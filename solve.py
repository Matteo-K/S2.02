#!/bin/env -S python3 -O

from src.board import Board
from src.solver import Solver
from sys import stderr
import argparse
import src.benchmarking as bch

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
    parser = argparse.ArgumentParser(
        description="Programme de test d'algorithmes de résolution du problème des N reines", epilog='S2.02')

    parser.add_argument('n', type=int, help='Constante N')
    parser.add_argument('algorithm', type=str,
                        help='Algorithme à utiliser. Supporte les expressions régulières.')
    parser.add_argument('-b', '--benchmark',
                        help="Mesurer la performance de l'algorithme au lieu de résoudre. La valeur de l'option donne le nombre d'exécutions (200 par défaut)", type=int, nargs='?', const=200, metavar='TIMES')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Afficher la sortie verbeuse")

    args = parser.parse_args()

    # Fetch the solver class
    valid_algorithms = list(bch.match_algorithms(args.algorithm))
    if len(valid_algorithms) == 0:
        print(f'Erreur: aucun algorithme correspondant à "{args.algorithm}" trouvé.', file=stderr)
        exit(1)
    if len(valid_algorithms) > 1:
        print(f'Erreur: {len(valid_algorithms)} algorithmes correspondant à "{args.algorithm}" trouvés. Donnez un expression régulière plus précise.', file=stderr)
        exit(1)

    solver = bch.retrieve_solver(valid_algorithms[0])

    if (args.benchmark):
        print(bch.benchmark(args.n, solver, args.verbose, args.benchmark))
    else:
        solve(args.n, solver)
