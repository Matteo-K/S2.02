#!/bin/env -S python3 -O

"""
Program to run or benchmark specific N-Queen solver algorithms.
"""

from src.board import Board
from typing import Optional, Any
import argparse as ap
import src.benchmarking as bch


def print_solution(n: int, solution: Optional[Any]):
    if solution is None:
        print('No solution')
    else:
        if not isinstance(solution, Board):
            print(solver.to_board(n, solution))
        print(solution)


if __name__ == '__main__':
    # Parse arguments
    parser = ap.ArgumentParser(description='Test and benchmark N-Queens problem solver algorithms.',
                               epilog=bch.EPILOG, formatter_class=bch.RawTextArgumentDefaultsHelpFormatter)

    parser.add_argument('n', type=int,
                        help='N value')
    parser.add_argument('algorithm', type=str, help='algorithm to use. Supports regular expressions.\nAvailable algorithms:\n' +
                        '\n'.join(f'  {algorithm}' for algorithm in bch.ALGORITHMS))
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='show verbose output')

    options_benchmarking = parser.add_argument_group('Benchmarking options')
    options_benchmarking.add_argument('-b', '--benchmark', action='store_true',
                                      help='benchmark instead of solving')
    options_benchmarking.add_argument('-c', '--count', default=200,
                                      type=bch.constrain(int, lambda n: n > 0, 'execution count must be greater than zero'),
                                      help='benchmarking execution count')
    options_benchmarking.add_argument('-d', '--duration',
                                      type=bch.constrain(float, lambda t: t > 0, 'duration must be greater than zero'),
                                      help='benchmarking duration (seconds)')
    args = parser.parse_args()

    chosen_algorithms = list(bch.match_algorithms(args.algorithm))
    if len(chosen_algorithms) == 0:
        parser.error(f'no algorithm matching "{args.algorithm}".')

    if (args.duration is None) == (args.count is None):
        parser.error("benchmarking count or duration (only one of the two) must be specified")

    benchmarking_strategy =\
        (bch.DurationBenchmarkingStrategy(args.duration / len(chosen_algorithms))
         if args.duration else
         bch.CountBenchmarkingStrategy(args.count))\
        if args.benchmark else\
        None

    for algorithm in chosen_algorithms:
        print(algorithm)
        solver = bch.get_solver(algorithm)

        if benchmarking_strategy:
            print(bch.benchmark(args.n, solver, args.verbose, benchmarking_strategy))
        else:
            print_solution(args.n, solver.solve(args.n))
