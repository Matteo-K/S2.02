# Importation des modules nécessaires
from src.board import Board
from src.helpers import is_valid
from src.solver import Solver
from typing import Optional
import random

# Définition de la classe PingPong qui hérite de la classe Solver


class PingPong(Solver):
    # Méthode statique solve qui résout le problème des N reines
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
        # Initialisation de la liste résultat avec des zéros
        res = [0 for _ in range(n)]
        # Boucle jusqu'à ce que la configuration soit valide
        while not is_valid(res):
            # Sélection d'un indice aléatoire
            index = random.randint(0, n-1)
            # Incrémentation de la valeur à cet indice et prise modulo n pour éviter les dépassements
            res[index] = (res[index]+1) % n
        # Renvoie la configuration valide
        return res

    # Méthode statique to_board qui convertit la solution en un objet Board
    @staticmethod
    def to_board(n: int, solution: list[int]) -> Board:
        # Création d'un objet Board
        board = Board(n)
        # Vérification de la longueur de la solution
        assert len(solution) == n
        # Parcours de la solution pour placer les reines sur le plateau
        for r, c in enumerate(solution):
            board[c, r] = False
        # Renvoie le plateau avec les reines placées
        return board
