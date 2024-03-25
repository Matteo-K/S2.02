from dataclasses import dataclass
from importlib import import_module
from math import log10
from statistics import mean, median
from sys import stderr
from typing import Optional, Iterable
import argparse as ap
import re
import time
import tracemalloc
from abc import ABC, abstractmethod

_solvers = {
    'backtracking_graphe': ('src.raphael.backtracking_graphe', 'BacktrackingGraphe'),
    'backtracking': ('src.raphael.backtracking', 'Backtracking'),
    'brute_force': ('src.matteo', 'BruteForce'),
    'echange': ('src.matteo', 'Exchange'),
    'mask': ('src.raphael.mask', 'Mask'),
    'min_conflicts': ('src.paolo.min_conflicts', 'MinConflicts'),
    'pingpong': ('src.marius.pingpong', 'PingPong'),
    'random': ('src.matteo', 'Random'),
    'symetrie': ('src.marius.symetrie', 'Symetrie'),
}
""" (solver module name, solver class name) by algorithm """

ALGORITHMS = _solvers.keys()


class RawTextArgumentDefaultsHelpFormatter(ap.RawTextHelpFormatter, ap.ArgumentDefaultsHelpFormatter):
    pass


class BenchmarkingStrategy(ABC):
    @abstractmethod
    def should_keep_going(self, times_executed_so_far: int, elapsed_seconds: float) -> bool:
        pass

    @abstractmethod
    def get_verbose_output_line(self, times_executed_so_far: int, elapsed_seconds: float) -> str:
        pass


class NumberOfTimesBenchmarkingStrategy(BenchmarkingStrategy):
    def __init__(self, number_of_times_to_execute: int):
        self.__nbot = number_of_times_to_execute
        self.__nbot_pad = int(log10(number_of_times_to_execute) + 1)

    def should_keep_going(self, times_executed_so_far: int, elapsed_seconds: float) -> bool:
        return times_executed_so_far < self.__nbot

    def get_verbose_output_line(self, times_executed_so_far: int, elapsed_seconds: float) -> str:
        return f'\r{str(times_executed_so_far).zfill(self.__nbot_pad)}/{self.__nbot} {elapsed_seconds:.1f}sec'


class DurationBenchmarkingStrategy(BenchmarkingStrategy):
    def __init__(self, benchmark_duration_seconds: float):
        self.__duration = benchmark_duration_seconds

    def should_keep_going(self, times_executed_so_far: int, elapsed_seconds: float) -> bool:
        return elapsed_seconds < self.__duration

    def get_verbose_output_line(self, times_executed_so_far: int, elapsed_seconds: float) -> str:
        # it took us elapsed_seconds to execute times_executed_so_far
        # how much time can we execute in elapsed_seconds
        expected_max_times = int(times_executed_so_far / elapsed_seconds * self.__duration)
        return f'\r{times_executed_so_far}/{expected_max_times} {elapsed_seconds:.1f}sec'


def match_algorithms(regex: str) -> Iterable[str]:
    return (algorithm for algorithm in ALGORITHMS if re.fullmatch(regex, algorithm) is not None)


def args_error(msg: str):
    print('Error:', msg, file=stderr)
    exit(1)


def get_solver(algorithm: str) -> Optional[type]:
    module_name, class_name = _solvers[algorithm]
    return getattr(import_module(module_name), class_name)


@dataclass(frozen=True)
class BenchmarkResult:
    """ Result of a benchmarking """
    avg_time: float
    """ Average CPU time (ms) """
    med_time: float
    """Median CPU time (ms)"""
    min_time: float
    """Minimum CPU time (ms)"""
    max_time: float
    """Maximum CPU time (ms)"""
    avg_mem: float
    """Average memory usage (bytes)"""
    med_mem: float
    """Median memory usage (bytes)"""
    min_mem: float
    """Minimum memory usage (bytes)"""
    max_mem: float
    """Maximum memory usage"""

    def __str__(self) -> str:
        def format(x) -> str:
            return f'{x:.3f}' if isinstance(x, float) else str(x)

        return '\n'.join(f'{kv[0]}: {format(kv[1])}' for kv in self.__dict__.items())


def benchmark(n: int, solver: type, verbose_output: bool, strategy: BenchmarkingStrategy) -> BenchmarkResult:
    durations: list[float] = []
    memories: list[int] = []

    start_human_time = time.time()

    while strategy.should_keep_going(len(durations), time.time() - start_human_time):
        start_time = time.process_time()
        tracemalloc.start()
        solver.solve(n)
        memory = tracemalloc.get_traced_memory()[1]
        memories.append(memory)
        tracemalloc.stop()
        duration = time.process_time() - start_time
        durations.append(duration * 1000)

        if verbose_output:
            print(strategy.get_verbose_output_line(len(durations), time.time() - start_human_time), file=stderr, end='')

    if verbose_output:
        print()

    return BenchmarkResult(
        mean(durations),
        median(durations),
        min(durations),
        max(durations),
        mean(memories),
        median(memories),
        min(memories),
        max(memories),
    )
