#!/bin/env python3

import sys
from importlib import import_module
from solver import Solver
from board import Board

if __name__ == '__main__':
    # solver module names by solver class names
    solvers = {'Backtracking': 'raphael.backtracking',
               'BacktrackingGraphe': 'raphael.backtracking_graphe'}

    def print_usage():
        print(f'Usage: {sys.argv[0]} <N> <technique_name>')

    # Resolve arguments
    if len(sys.argv) != 3:
        print_usage()
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print(f'Error: N must be an integer')
        print_usage()
        exit(1)

    solver_class_name = sys.argv[2]
    if solver_class_name not in solvers:
        print(f'Error: unknown solver "{solver_class_name}"')
        print('Available solvers:', *solvers.keys())
        exit(1)

    # Fetch the solver class
    solver: Solver = getattr(import_module(
        solvers[solver_class_name]), solver_class_name)

    # Solve
    solution = solver.solve(n)
    if not isinstance(solution, Board | str):
        print(solver.toBoard(n, solution) or "No solution")
    print(solution)
