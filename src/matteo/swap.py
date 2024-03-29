"""
Algorithme d'échange
"""

from src.helpers import is_valid
from src.solver import SolverRowList
from typing import Optional
import random


class Swap(SolverRowList):
    @staticmethod
    def solve(n: int) -> Optional[list[int]]:
        """
        Créer une liste de valeur de 0 à n, 
        si la liste est bonne :
            - renvoie le résultat correcte
        sinon 
            - prend un indice aléatoire
            - échange les valeurs entre l'indice et l'indice au-dessus

        paramètre :
        -----------
        n : int
        nombre de reine

        renvoie :
        ---------
        res : list
        tableau des positions des reines par colonnes
        """
        res = [i for i in range(n)]
        while not is_valid(res):
            index = random.randint(0, n-1)
            res[index], res[(index+1) % n] = res[(index+1) % n], res[index]
        return res
