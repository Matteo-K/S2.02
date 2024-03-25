"""
Techniques de Ping pong (Marius)
"""

from src.board import Board
from src.helpers import is_valid
from src.solver import Solver
from typing import Optional
import random


class PingPong(Solver):
    @staticmethod
    def solve(n: int) -> list[Optional[int]]:
        """
        Créer une liste de 0 de taille n, 
        si la liste est bonne :
            - renvoie le résultat correcte
        sinon 
            - prend un indice aléatoire
            - Complète le tableau de résultat par incrémentation de 1

        paramètre :
        -----------
        n : int
        nombre de reines

        renvoie :
        ---------
        res : list
        tableau des positions des reines par colonnes
        """
        res = [0 for _ in range(n)]
        while not is_valid(res):
            index = random.randint(0, n-1)
            res[index] = (res[index]+1) % n
        return res

    @staticmethod
    def to_board(n: int, solution: list[int]) -> Board:
        board = Board(n)
        assert len(solution) == n
        for r, c in enumerate(solution):
            board[c, r] = False
        return board
