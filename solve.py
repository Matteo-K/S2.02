#!/bin/env -S python3 -O

"""
Program to run or benchmark specific N-Queen solver algorithms.
"""

from src.board import Board
from src.solver import Solver
from typing import Optional, Any
import argparse as ap
import src.benchmarking as bench


def print_solution(n: int, solution: Optional[Any]):
    if solution is None:
        print('No solution')
    else:
        if not isinstance(solution, Board):
            print(solver.to_board(n, solution))
        print(solution)


if __name__ == '__main__':
    # Parse arguments
    parser = ap.ArgumentParser(
        description='Test and benchmark N-Queens problem solver algorithms.', epilog='S2.02', formatter_class=bench.RawTextArgumentDefaultsHelpFormatter)

    parser.add_argument('n', type=int,
                        help='N value')
    parser.add_argument('algorithm', type=str,
                        help='algorithm to use. Supports regular expressions.\nAvailable algorithms:\n' + '\n'.join(f'  {algorithm}' for algorithm in bench.ALGORITHMS))
    parser.add_argument('-b', '--benchmark-times', type=int, nargs='?', const=200, metavar='TIMES',
                        help='benchmark instead of solving. The value is the execution count')
    parser.add_argument('-d', '--benchmark-duration', type=float, metavar='DURATION',
                        help='benchmark instead of solving. The value is the benchmark duration (seconds)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='show verbose output')

    args = parser.parse_args()

    chosen_algorithms = list(bench.match_algorithms(args.algorithm))
    if len(chosen_algorithms) == 0:
        bench.args_error(f'no algorithm matching "{args.algorithm}".')

    benchmarking_strategy =\
        bench.DurationBenchmarkingStrategy(args.benchmark_duration / len(chosen_algorithms)) if args.benchmark_duration\
        else bench.NumberOfTimesBenchmarkingStrategy(args.benchmark_times) if args.benchmark_times\
        else None

    for algorithm in chosen_algorithms:
        print(algorithm)
        solver = bench.get_solver(algorithm)

        if (benchmarking_strategy):
            print(bench.benchmark(args.n, solver, args.verbose, benchmarking_strategy))
        else:
            print_solution(args.n, solver.solve(args.n))
