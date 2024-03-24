from dataclasses import dataclass
from importlib import import_module
from statistics import mean, median
from sys import stderr
from typing import Optional, Iterable
import re
import time
import tracemalloc

_solvers = {
    'backtracking_graphe': ('src.raphael.backtracking_graphe', 'BacktrackingGraphe'),
    'backtracking': ('src.raphael.backtracking', 'Backtracking'),
    'brute_force': ('src.matteo', 'BruteForce'),
    'echange': ('src.matteo', 'Exchange'),
    'random': ('src.matteo', 'Random'),
    'min_conflicts': ('src.paolo.min_conflicts', 'MinConflicts'),
    'mask': ('src.raphael.mask', 'Mask'),
    'pingpong': ('src.marius', 'PingPong')
}
""" (solver module name, solver class name) by algorithm """

ALGORITHMS = _solvers.keys()

def match_algorithms(regex: str) -> Iterable[str]:
    return (algorithm for algorithm in ALGORITHMS if re.fullmatch(regex, algorithm) is not None)

def retrieve_solver(algorithm: str) -> Optional[type]:
    module_name, class_name = _solvers[algorithm]
    return getattr(import_module(module_name), class_name)

@dataclass
class BenchmarkingResult:
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


def benchmark(n: int, solver: type, verbose_output: bool, times: int) -> BenchmarkingResult:
    durations: list[float] = []
    memories: list[int] = []

    for i in range(times):
        start_time = time.process_time()

        tracemalloc.start()
        solver.solve(n)
        memory = tracemalloc.get_traced_memory()[1]
        memories.append(memory)
        tracemalloc.stop()
        duration = time.process_time() - start_time
        durations.append(duration * 1000)

        if verbose_output:
            print(f'{i+1}. {duration:.4f}ms, {memory}b', file=stderr)

    return BenchmarkingResult(
        mean(durations),
        median(durations),
        min(durations),
        max(durations),
        mean(memories),
        median(memories),
        min(memories),
        max(memories),
    )
