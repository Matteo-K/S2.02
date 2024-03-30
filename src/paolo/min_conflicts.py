"""
Algorithme des conflits minimum

"""

from src.solver import SolverRowList
from typing import Optional
from random import choice


class MinConflicts(SolverRowList):
    """
       La  classe MinConflits qui a toutes le méthodes utilisées pour l'algorithme des min-conflits

        L'algorithme de min conflits consite a placer une première reine, de manière aléatoire, sur la première colonne d'un échiquier vide, 
        et on note toutes les cases mises en danger par cette reine.
        Puis quand on place la deuxieme reine dans la deuxième colonne on prend on compte les cases mises en danger
        et on place cette nouvelle reine dans une des cases mise le moins en danger, puis on note encoretoutes les cases mises en danger en augmantant la sévérité du danger
        des cases déja en danger. On continue cette approche jusqu'à que toutes les reines soient placées.


    """
    @staticmethod
    def solve(n: int) -> Optional[list[int]]:
        """
            ceci est l'algorithme principal
        """
        fin = False
        # initialisation de la liste des coordonnées des reines,
        # l'indice de la liste correspond au numero de colonne d'une reine, et la valeur à son numero de ligne
        listeR = [None for i in range(n)]

        while not fin:
            # réinitialisation
            listeR = [None for i in range(n)]

            # initialisation d'une grille de conflits
            conf = MinConflicts.conflicts(n, listeR)

            # pour toutes les colonnes on place une reine sur le scases
            # où on trouve le moins de conflits
            for i in range(n):
                # res est le numero de ligne de la nouvelle reine placée
                # la grille de conflits conf est utilisée dans la methode place()
                # pour trouver
                res = MinConflicts.place(i, conf)
                listeR[i] = res  # la reine est placée
                # la liste des conflits est encore crée avec la nouvelle reine
                conf = MinConflicts.conflicts(n, listeR)

            fin = MinConflicts.valide(conf, listeR)  # on vérifie si aucune des reines sont en danger

        return listeR  # on retourne la liste des solutions

    @staticmethod
    def conflicts(n: int, listeR: list[Optional[int]]) -> list[list[int]]:
        """
            Méthode renvoie tableau des conflits celon la liste de placement des reines.

            Elle prend en paramètre la taille de l'echiquier et les coordonnées des reines placées.

            Le tableau de conflits est un tableau de taille N*N quienregiste les conflits d'un échiquier,
            par exemple si un reine est placée, les lignes, collonnes et diagonales de la reine sont un danger pour les autres reines,
            donc ces cases sont en conflit (on modélise cela en ajoutant un 1 pour toutes ces cases, si une autre reine est placée on augmenterai les conflits de ces cases).

            Puisque les reines ne peuvent être sur la même colonne on ne compte pas les conflits des colonnes et une reine ne peut se mettre en danger
            donc la case où est placée la reine n'est pas en conflit.  
        """
        conf = [[0 for i in range(n)] for i in range(n)]
        for ind in range(len(listeR)):
            r = listeR[ind]  # prend le numero de ligne de la reine de colonne ind

            if r != None:  # si reine est placée alors:
                for i in range(n):
                    # la case où est mise la reine n'est pas en conflit
                    if (i != ind):
                        conf[r][i] += 1

                # les conflits de la diagonale vers le bas
                for i in range(n):
                    diag = r+i-ind
                    if (diag < n) and (i != ind):
                        if diag > -1:
                            conf[diag][i] += 1
                # les conflits de la diagonale vers le haut
                for i in range(n):
                    diag = (r-i+ind) % n
                    if ((r-i+ind) < n) and (i != ind):
                        if (r-i+ind) > -1:
                            conf[diag][i] += 1

        return conf

    @staticmethod
    def place(indice: int, conf: list[list[int]]):
        """
            Méthode pour placer une reine dans la case d'une colonne avec le moins de conflits.
            Elle sert à trouver la case où il y le moins de conflits, la methode ne place pas réelement la reine,
            la méthode renvoie la ligne du placement de la reine

            La méthode prend en paramètre l'indice de colonne de la reine à placer et le tableau des conflits
        """
        taille = len(conf)
        min = 999
        indiceMin = []  # liste des cases dont le conflit est minimum

        for i in range(taille):
            if conf[i][indice] < min:  # si une case à moins de conflits que min, la liste indiceMin est voidée et on y ajoute l'indice ce la nouvelle case
                min = conf[i][indice]
                indiceMin = []
                indiceMin.append(i)
            # si une case a un nombre de conflit(s) egal à la case de conflit minimal, on ajoute son indice à la liste de cases de conflit minimaux
            elif conf[i][indice] == min:
                indiceMin.append(i)
        return choice(indiceMin)  # une des cases dont le conflit est minimum est choisie aléatoirement

    @staticmethod
    def valide(conf: list[list[int]], coordsReines) -> bool:
        """
            Méthode de validation de solution, si les reines sont bien placées on retourne True, sinon False

            La méthode prend en paramètre la grille des conflits et la liste des coordonées des reines
        """
        res = True
        taille = len(coordsReines)
        i = 0
        while (res) and (i < taille):
            # si dans la grille de conflits l'eplacement de la reine est en conflit, donc supérieur à 0,
            # l'échiquier n'a pas été remplit correctement
            if conf[coordsReines[i]][i] != 0:
                res = False
            i += 1
        return res
