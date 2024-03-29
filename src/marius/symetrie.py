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
                    if queens[i][0] == queens[j][0]\
                            or queens[i][1] == queens[j][1]\
                            or abs(queens[i][1] - queens[j][1]) == abs(queens[i][0] - queens[j][0]):
                        return False
            return True

        # queens = [0 for _ in range(N)]  # position des reines à 0
        queens = []

        # on commence le trie par la reine la plus à gauche
        indice_ligne = 0
        indice_colonne = 0

        # on continue tant que l'echiquier n'est pas valide et que toutes les reines ne sont pas posées
        # print(is_valid_clg(queens))
        while (len(queens) < n):
            # boucle qui cherche à poser les une reine dans la colonne
            while (indice_ligne < n):
                if (impaire) and (indice_colonne == (n//2)):
                    # on pose la reine et son opposé
                    queens.append([indice_ligne, indice_colonne])
                    if not is_valid_clg(queens):

                        queens = queens[:-1]
                        indice_ligne += 1

                    else:
                        break
                else:
                    queens.append([indice_ligne, indice_colonne])
                    queens.append([n - 1 - indice_ligne, n - 1 - indice_colonne])

                # si le positionnement n'est pas valide on enlève les reines
                # précédament posées
                # et on passe à la ligne suivante
                    if not is_valid_clg(queens):

                        queens = queens[:-2]
                        indice_ligne += 1

                    else:
                        break

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

        return queens

    @staticmethod
    def to_board(n: int, solution: Any) -> Board:
        b = Board(n)
        if solution is not None:
            for i in range(n):
                b[solution[i][0], solution[i][1]] = False
        return b
