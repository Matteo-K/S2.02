#!/bin/env -S python3 -O

from src.board import Board
from src.solver import Solver
import argparse as ap
import src.benchmarking as bench


def solve(n: int, solver: Solver):
    solution = solver.solve(n)
    if solution is None:
        print("No solution")
    else:
        if not isinstance(solution, Board):
            print(solver.toBoard(n, solution))
        print(solution)


if __name__ == '__main__':
    # Parse arguments
    parser = ap.ArgumentParser(
        description="Test and benchmark N-Queens problem algorithms", epilog='S2.02', formatter_class=bench.RawTextArgumentDefaultsHelpFormatter)

    parser.add_argument('n', type=int,
                        help='N value')
    parser.add_argument('algorithm', type=str,
                        help='algorithm to use. Supports regular expressions.\nAvailable algorithms:\n' + '\n'.join(f'  {algorithm}' for algorithm in sorted(bench.ALGORITHMS)))
    parser.add_argument('-b', '--benchmark', type=int, nargs='?', const=200, metavar='TIMES',
                        help="benchmark algorithm instead of solving. The value is the execution count")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="show verbose output")

    args = parser.parse_args()

    # Fetch the solver class
    valid_algorithms = list(bench.match_algorithms(args.algorithm))
    if len(valid_algorithms) == 0:
        bench.args_error(f'no algorithm matching "{args.algorithm}".')
    if len(valid_algorithms) > 1:
        bench.args_error(f'{len(valid_algorithms)} algorithms matching "{args.algorithm}". Use a more precise regular expression.')

    solver = bench.get_solver(valid_algorithms[0])

    if (args.benchmark):
        print(bench.benchmark(args.n, solver, args.verbose, args.benchmark))
    else:
        solve(args.n, solver)
