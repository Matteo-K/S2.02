#!/bin/env -S python3 -O

from itertools import chain
import argparse
import matplotlib.pyplot as plt
import src.benchmarking as bch

# ./graph.py memory 4 -n 200 mask backtracking_graphe
# ./graph.py time 4 -n 200 mask backtracking_graphe
# ./graph.py time 4 -n 200 mask backtracking.*
# ./graph.py time 4 -n 200 mask .*

# ./graphy {mem,time} N [OPTION]... [ALGORITHM]...

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Créer des graphiques MPL de benchmarking des algorithmes", epilog='S2.02')
    
    parser.add_argument('criterion', help='Critères de performance', choices=('memory', 'time'))
    parser.add_argument('-n', type=int, help='Constante N')
    parser.add_argument('algorithms', nargs='+', metavar='ALGORITHM', help='Algorithmes à mesurer (chacun aura sa courbe sur le graphique). Supprote les expressions régulières.')
    parser.add_argument('-v', 
    '--verbose', action='store_true', help="Afficher la sortie verbeuse")

    args = parser.parse_args()

    choosen_algorithms = set(chain.from_iterable((bch.match_algorithms(regex) for regex in args.algorithms)))

    


