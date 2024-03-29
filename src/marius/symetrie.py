"""
Techniques de symétrie (Marius)
"""

from src.solver import Solver
from typing import Any
from src.board import Board


class Symetrie(Solver):
    @staticmethod
    def solve(n: int) -> Any:
        impaire = n % 2 == 1

        def is_valid_clg(queens: list) -> bool:
            """
            vérifie si la liste de résultat est valide au problème

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
                    # Vérifie si deux reines sont sur la même ligne, la même colonne ou sur la même diagonale
                    if queens[i][0] == queens[j][0]\
                            or queens[i][1] == queens[j][1]\
                            or abs(queens[i][1] - queens[j][1]) == abs(queens[i][0] - queens[j][0]):
                        return False
            return True

        # Initialisation de la liste pour stocker les positions des reines
        queens = []

        # On commence le tri par la reine la plus à gauche
        indice_ligne = 0
        indice_colonne = 0

        # On continue tant que l'échiquier n'est pas valide et que toutes les reines ne sont pas posées
        while (len(queens) < n):
            # Boucle qui cherche à poser les reines dans la colonne
            while (indice_ligne < n):
                # Si n est impair et que l'on est à la colonne centrale, on pose seulement une reine
                if (impaire) and (indice_colonne == (n//2)):
                    # Si n est impair et que l'on est à la colonne centrale, on pose seulement une reine
                    queens.append([indice_ligne, indice_colonne])
                    if is_valid_clg(queens):
                        break
                    else:
                        queens = queens[:-1]
                        indice_ligne += 1
                else:
                    queens.append([indice_ligne, indice_colonne])
                    queens.append([n - 1 - indice_ligne, n - 1 - indice_colonne])

                    # Si le positionnement n'est pas valide, on enlève la/les reine(s) précédemment posée(s) et on passe à la ligne suivante
                    if is_valid_clg(queens):
                        break
                    else:
                        queens = queens[:-2]
                        indice_ligne += 1

            # Si toutes les reines ont été placées, passe à la colonne suivanteet réinitialise l'indice de ligne.
            # Sinon, retire les reines placées et on continue la progression de "indice_ligne".
            if indice_ligne >= n:
                if (impaire) and (indice_colonne == (n//2)):
                    indice_ligne = queens[-1][0]+1
                    queens = queens[:-1]
                else:
                    indice_ligne = queens[-2][0]+1
                    queens = queens[:-2]
                indice_colonne -= 1
            else:
                indice_colonne += 1
                indice_ligne = 0

        # Renvoie la liste contenant les positions des reines
        return queens

    @staticmethod
    def to_board(n: int, solution: Any) -> Board:
        b = Board(n)
        if solution is not None:
            for i in range(n):
                b[solution[i][0], solution[i][1]] = False
        return b
