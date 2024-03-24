#!/bin/env -S python3 -O

from sys import stderr
import tracemalloc
import time
import argparse
from statistics import mean, median
from importlib import import_module
from src.solver import Solver
from src.board import Board


def solve(n: int, solver: Solver):
    solution = solver.solve(n)
    if solution is None:
        print("No solution")
    else:
        if not isinstance(solution, Board):
            print(solver.toBoard(n, solution))
        print(solution)


def benchmark(n: int, solver: Solver, verbose_output: bool, times: int):
    durations: list[float] = []
    memories: list[int] = []

    def fmt_float(x) -> str:
        return f'{float(x):.3f}'

    def fmt_int(x) -> str:
        return str(int(x))

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
            print(f'{i+1}. {fmt_float(duration)}s, {fmt_int(memory)}', file=stderr)

    results = {
        "Avg time (ms)": fmt_float(mean(durations)),
        "Median time (ms)": fmt_float(median(durations)),
        "Min time (ms)": fmt_float(min(durations)),
        "Max time (ms)": fmt_float(max(durations)),
        "Avg memory (bytes)": fmt_float(mean(memories)),
        "Median memory (bytes)": fmt_float(median(memories)),
        "Min memory (bytes)": fmt_int(min(memories)),
        "Max memory (bytes)": fmt_int(max(memories)),
    }

    for key, value in results.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    # (solver module name, solver class name) by algorithm
    solvers = {
        'backtracking_graphe': ('raphael.backtracking_graphe', 'BacktrackingGraphe'),
        'backtracking': ('raphael.backtracking', 'Backtracking'),
        'brute_force': ('matteo', 'BruteForce'),
        'echange': ('matteo', 'Exchange'),
        'random': ('matteo', 'Random'),
        'min_conflicts': ('paolo.min_conflicts', 'MinConflicts'),
        'mask': ('raphael.mask', 'Mask'),
        'pingpong': ('marius', 'PingPong')
    }

    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Programme de test d'algorithmes de résolution du problème des N reines", epilog='S2.02')

    parser.add_argument('n', type=int, help='Constante N')
    parser.add_argument('algorithm', type=str,
                        help='Algorithme à utiliser', choices=solvers.keys())
    parser.add_argument('-b', '--benchmark',
                        help="Mesurer la performance de l'algorithme au lieu de résoudre. La valeur de l'option donne le nombre d'exécutions (200 par défaut)", type=int, nargs='?', const=200, metavar='TIMES')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Afficher la sortie verbeuse")

    args = parser.parse_args()

    # Fetch the solver class
    module_name, class_name = solvers[args.algorithm]
    solver: Solver = getattr(import_module(
        'src.'+module_name), class_name)

    # Solve
    if (args.benchmark):
        benchmark(args.n, solver, args.verbose, args.benchmark)
    else:
        solve(args.n, solver)
