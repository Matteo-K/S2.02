from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass
from importlib import import_module
from math import log10
from statistics import mean, median
from sys import stderr
from typing import Optional, Iterable, Any, TypeVar, Callable, Sequence, Collection
import argparse as ap
import re
import time
import tracemalloc

EPILOG = 'S2.02 C4'

_solvers = {
    'backtracking_graphe': ('src.raphael.backtracking_graphe', 'BacktrackingGraphe'),
    'backtracking': ('src.raphael.backtracking', 'Backtracking'),
    'brute_force': ('src.matteo.brute_force', 'BruteForce'),
    'swap': ('src.matteo.swap', 'Swap'),
    'mask': ('src.raphael.mask', 'Mask'),
    'min_conflicts': ('src.paolo.min_conflicts', 'MinConflicts'),
    'pingpong': ('src.marius.pingpong', 'PingPong'),
    'random': ('src.matteo.random', 'Random'),
    'symetrie': ('src.marius.symetrie', 'Symetrie'),
}
"""algorithm -> (solver module name, solver class name)"""

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


class CountBenchmarkingStrategy(BenchmarkingStrategy):
    def __init__(self, count: int):
        self.__count = count
        self.__count_padding = int(log10(count) + 1)

    def should_keep_going(self, times_executed_so_far: int, elapsed_seconds: float) -> bool:
        return times_executed_so_far < self.__count

    def get_verbose_output_line(self, times_executed_so_far: int, elapsed_seconds: float) -> str:
        return f'\r{str(times_executed_so_far).zfill(self.__count_padding)}/{self.__count} {elapsed_seconds:.1f}s'


class DurationBenchmarkingStrategy(BenchmarkingStrategy):
    def __init__(self, benchmark_duration_seconds: float):
        self.__duration = benchmark_duration_seconds

    def should_keep_going(self, times_executed_so_far: int, elapsed_seconds: float) -> bool:
        return elapsed_seconds < self.__duration

    def get_verbose_output_line(self, times_executed_so_far: int, elapsed_seconds: float) -> str:
        # it took us elapsed_seconds to execute times_executed_so_far
        # how much time can we execute in elapsed_seconds
        expected_max_times = int(times_executed_so_far / elapsed_seconds * self.__duration)
        return f'\r{times_executed_so_far}/{expected_max_times} {elapsed_seconds:.1f}s/{self.__duration:.1f}s'


def match_algorithms(regex: str) -> Iterable[str]:
    return (algorithm for algorithm in ALGORITHMS if re.fullmatch(regex, algorithm) is not None)


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


@dataclass(frozen=True)
class Benchmark:
    min_n: int
    result: dict[str, list[BenchmarkResult]]


def benchmark(n: int, solver: type, verbose_output: bool, strategy: BenchmarkingStrategy) -> BenchmarkResult:
    durations: list[float] = []
    memories: list[int] = []
    solutions: list[Any] = []

    benchmark_start_instant = time.time()

    while strategy.should_keep_going(len(durations), time.time() - benchmark_start_instant):
        execution_start_process_time = time.process_time()
        tracemalloc.start()
        solution = solver.solve(n)
        memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        duration = time.process_time() - execution_start_process_time
        solutions.append(solution)
        memories.append(0 if solution is None else memory)
        durations.append(0 if solution is None else duration * 1000)

        if verbose_output:
            print(strategy.get_verbose_output_line(len(durations), time.time() - benchmark_start_instant), file=stderr, end='')

    if verbose_output:
        print(file=stderr)

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


def transform_char(string: str, index: int, transform: Callable[[str], str]) -> str:
    return string[:index] + transform(string[index]) + string[index + 1:]


def fields_arg(fields: Collection[str]) -> ap.Action:
    # Find the field letter index
    for i in range(min(map(len, fields))):
        if len({field[i] for field in fields}) == len(fields) and all(field[i].isalpha() for field in fields):
            break
    else:
        raise ValueError("Couldn't find an index for distinct field letters")

    field_letters = {field[i].casefold(): field for field in fields}

    helpstr = 'show (uppercase), or hide (lowercase) fields:\n' + ''.join(
        f'  {letter} as in {transform_char(field, i, str.upper)}\n'
        for letter, field in field_letters.items())

    class FieldsAction(ap.Action):
        def __init__(self, help: str = None, **kwargs):
            super().__init__(help=help or '' + helpstr,
                             **kwargs)

        def __call__(self,
                     parser: ap.ArgumentParser,
                     namespace: ap.Namespace,
                     values: Optional[str | Sequence[Any]],
                     option_string: Optional[str]) -> None:
            setattr(namespace, self.dest, self.__parse(values))

        def __parse(self, field_arg: str) -> dict[str, bool]:
            if Counter(field_arg.casefold()) != {letter: 1 for letter in field_letters}:
                raise ap.ArgumentError(self, f'argument must contain every field letter ({", ".join(field_letters)}) once')

            return {field_letters[l.casefold()]: l.isupper() for l in field_arg}

    return FieldsAction


_T = TypeVar('_T')


def constrain(parser: Callable[[str], _T], constraint: Callable[[_T], bool], msg=None) -> Callable[[str], _T]:
    def parse(arg: str):
        res = parser(arg)
        if not constraint(res):
            raise ap.ArgumentTypeError(f"{msg or 'Constraint failed'} (got {res})")
        return res
    return parse


def interval_arg_type(min_min: int, separator: str) -> Callable[[str], tuple[int, Optional[int]]]:
    """ Parses a range. Returns a tuple containing the minimum minimum (or min_min if not present), and the maximum (or None if not present) """
    def parse(arg: str) -> range:
        comps = arg.split(separator, maxsplit=1)
        try:
            match len(comps):
                case 1:
                    min, max = int(comps[0]) if comps[0] else min_min, None
                case 2:
                    min, max = (int(comps[0]) if comps[0] else min_min,
                                int(comps[1]) if comps[1] else None)
                case _:
                    raise ap.ArgumentTypeError('incorrect range')
            if max is not None and min > max:
                raise ap.ArgumentTypeError(f'incorrect decreasing range: min ({min}) is greater than max ({max})')
            if min < min_min:
                raise ap.ArgumentTypeError(f'minimum value ({min}) is too small (expected at least {min_min})')
            return min, max
        except ValueError as e:
            raise ap.ArgumentTypeError(*e.args) from e
    return parse


def re_is_valid(pattern: str) -> bool:
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False
