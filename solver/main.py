#!/bin/env python3

import sys
from importlib import import_module


if __name__ == '__main__':
    solvers = 'backtracking', 'backtracking_graphe'

    def print_usage():
        print(f'Usage: {sys.argv[0]} <N> <technique_name>')
    

    if len(sys.argv) != 3:
        print_usage()
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print(f'Error: N must be an integer')
        print_usage()
        exit(1)

    solver = sys.argv[2]
    if solver not in solvers:
        print(f'Error: unknown solver "{solver}"')
        print('Available solvers:', solvers)
        exit(1)
    
    solverModule = import_module(solver)

    solution = solverModule.solve(n)
    print(solverModule.toBoard(n, solution))
    print(solution)

