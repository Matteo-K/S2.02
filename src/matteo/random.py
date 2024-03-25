"""
Algorithme aléatoire
"""

from src.helpers import is_valid
from src.solver import SolverRowList
from typing import Optional
import random


class Random(SolverRowList):
    @staticmethod
    def solve(n: int) -> Optional[list[int]]:
        """
        Résolution du problème par aléatoire
        Complète le tableau de résultat aléatoirement
        un chifre ne peut pas être présent deux fois dans le résultat
        continue en boucle tant que le résultat n'est correcte

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
        while progress:
            values = list(range(n))
            res = []
            compteur = n-1
            while compteur > -1:
                id = random.randint(0, compteur)
                res.append(values.pop(id))
                compteur -= 1
            progress = False if is_valid(res) else True
        return res
