"""
Technique de Min Conflicts de Paolo
"""

from src.solver import SolverRowList
from typing import Optional
from random import choice


class MinConflicts(SolverRowList):
    @staticmethod
    def solve(size: int) -> Optional[list[int]]:
        fin = False
        listeR = [None for i in range(size)]

        while not fin:
            # initialisation
            listeR = [None for i in range(size)]

            conf = MinConflicts.conflicts(size, listeR)
            for i in range(size):
                res = MinConflicts.place(i, conf)
                listeR[i] = res
                conf = MinConflicts.conflicts(size, listeR)

            fin = MinConflicts.valide(conf, listeR)

        return listeR

    @staticmethod
    def conflicts(n: int, listeR: list[Optional[int]]) -> list[list[int]]:
        # fonction renvoi tableau des conflits
        conf = [[0 for i in range(n)] for i in range(n)]
        for ind in range(len(listeR)):
            r = listeR[ind]
            if r != None:
                for i in range(n):
                    # la case ou est mise la reine n'est pas en conflit
                    if (i != ind):
                        conf[r][i] += 1

                # diagonale vers le bas
                for i in range(n):
                    diag = r+i-ind
                    if (diag < n) and (i != ind):
                        if diag > -1:
                            conf[diag][i] += 1
                # diagonale vers le haut
                for i in range(n):
                    diag = (r-i+ind) % n
                    if ((r-i+ind) < n) and (i != ind):
                        if (r-i+ind) > -1:
                            conf[diag][i] += 1

        return conf

    @staticmethod
    # fonction pour placer une reine dans la case d'une colonne avec le moins de conflits
    # fonction renvoie la ligne du placement de la reine
    # prend en paramètre l'indice de la colonne et le tableau des conflits
    def place(indice: int, conf: list[list[int]]):
        taille = len(conf)
        min = 999
        indiceMin = []
        for i in range(taille):
            if conf[i][indice] < min:
                min = conf[i][indice]
                indiceMin = []
                indiceMin.append(i)
            elif conf[i][indice] == min:
                indiceMin.append(i)
        return choice(indiceMin)

    @staticmethod
    def valide(conf: list[list[int]], coordsReines) -> bool:
        res = True
        taille = len(coordsReines)
        i = 0
        while (res) and (i < taille):
            if conf[coordsReines[i]][i] != 0:
                res = False
            i += 1
        return res
