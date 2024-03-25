"""
Algorithme de force brute
"""

from src.helpers import is_valid
from src.solver import SolverRowList
from typing import Optional


class BruteForce(SolverRowList):
    @staticmethod
    def solve(n: int) -> Optional[list[int]]:
        """
        Résolution du problème par brute force
        Complète le tableau de résultat par incrémentation par 1

        paramètre :
        -----------
        n : int
        nombre de reine

        renvoie :
        ---------
        res : list
        tableau des positions des reines par colonnes
        chaque valeur correspond au numéro de ligne
        l'indice correspond au numéro de colonne
        """
        progress = True
        res = [0 for _ in range(n)]
        # tant que le tableau n'est pas correct
        while progress:
            if is_valid(res):
                progress = False
            else:
                # incrémentation des valeurs
                res[0] = res[0]+1
                for i in range(0, n-1):
                    res[i+1] += res[i]//n
                    res[i] = res[i] % n
        return res
