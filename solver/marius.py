"""
Techniques de Marius
"""

from solver import Solver
from typing import Optional
from board import Board
import random

def is_valid(queens: list[int]) -> bool:
    """
    vérifie si la liste de résultat est valide au problème

    vérification des colonnes
        - queens[i] == queen[j] : vérifie si deux reines sont sur la même colonne

    vérification de la diagonale
        - abs(queens[i] - queens[j]) vérifie si la différence verticale entre les reines 
        - j - i : vérifie la différence horizontale

    paramètre :
    -----------
    queens : list
    liste des cordonnées de placement des reines

    renvoie :
    ---------
    bool
    True si la grille est valide au problème
    False sinon
    """
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(j - i):
                return False
    return True

class PingPong(Solver):
    @staticmethod
    def solve(size:int) -> list[Optional[int]]:
        """
        Créer une liste de 0 de taille size, 
        si la liste est bonne :
            - renvoie le résultat correcte
        sinon 
            - prend un indice aléatoire
            - Complète le tableau de résultat par incrémentation de 1

        paramètre :
        -----------
        size : int
        nombre de reine

        renvoie :
        ---------
        res : list
        tableau des positions des reines par colonnes
        """
        res = [0 for _ in range(size)]
        while not is_valid(res):
            index = random.randint(0, size-1)
            res[index] = (res[index]+1)%size
        return res
    
    @staticmethod
    def toBoard(n: int, solution: list[int]) -> Board:
        board = Board(n)
        assert len(solution) == n
        for r, c in enumerate(solution):
            board[c, r] = False
        return board
        