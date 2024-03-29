from src.board import Board
from typing import Any
from src.solver import Solver


"""
Techniques de symétrie (Marius)
"""
# Ce programme Python résout le problème des N reines en utilisant une approche de backtracking et en plaçant les reines 2 par 2 par symétrie.


class Symetrie(Solver):
    # La méthode solve est la fonction principale qui résout le problème des N reines.
    @staticmethod
    def solve(n: int) -> Any:

        # Fonction interne pour vérifier si la configuration actuelle des reines est valide.
        def is_valid_clg(queens: list) -> bool:
            """
            Vérifie si la liste de résultat est valide au problème
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
                    # Vérifie si deux reines sont sur la même ligne, la même colonne ou sur la même diagonale.
                    if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][1] - queens[j][1]) == abs(queens[i][0] - queens[j][0]):
                        return False
            return True

        # Initialisation de la liste pour stocker les positions des reines et des variables pour suivre la position actuelle.
        queens = []
        indice_ligne = 0
        indice_colonne = 0

        # Boucle principale pour placer les reines sur le plateau.
        while (len(queens) < n):
            while (indice_ligne < n):
                # Tente de placer deux reines à la fois, une sur la diagonale principale et l'autre sur la diagonale opposée.
                queens.append([indice_ligne, indice_colonne])
                queens.append([n - 1 - indice_ligne, n - 1 - indice_colonne])

                # Si la configuration n'est pas valide, retire les reines placées et incrémente l'indice de ligne.
                if not is_valid_clg(queens):
                    queens = queens[:-2]
                    indice_ligne += 1
                else:
                    break
            # Si toutes les reines ont été placées, passe à la colonne suivanteet réinitialise l'indice de ligne.
            # Sinon, retire les reines placées et on continue la progression de "indice_ligne".
            if indice_ligne >= n:
                indice_colonne -= 1
                indice_ligne = queens[-2][0]+1
                queens = queens[:-2]
            else:
                indice_colonne += 1
                indice_ligne = 0
        # Renvoie la liste contenant les positions des reines.
        return queens

    @staticmethod
    def to_board(n: int, solution: Any) -> Board:
        b = Board(n)
        if solution is not None:
            for i in range(n):
                b[solution[i][0], solution[i][1]] = False
        return b
