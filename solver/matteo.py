"""
Techniques de résolution de Mattéo
"""

import random

from solver import SolverRowList
from typing import Optional

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

class Random(SolverRowList):
    @staticmethod
    def solve(size: int) -> Optional[list[int]]:
        """
        Résolution du problème par aléatoire
        Complète le tableau de résultat aléatoirement
        un chifre ne peut pas être présent deux fois dans le résultat
        continue en boucle tant que le résultat n'est correcte

        paramètre :
        -----------
        size : int
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
            values = list(range(size))
            res = []
            compteur = size-1
            while compteur > -1:
                id = random.randint(0, compteur)
                res.append(values.pop(id))
                compteur -= 1
            progress = False if is_valid(res) else True
        return res

class BruteForce(SolverRowList):
    @staticmethod
    def solve(size: int) -> Optional[list[int]]:
        """
        Résolution du problème par brute force
        Complète le tableau de résultat par incrémentation par 1

        paramètre :
        -----------
        size : int
        nombre de reine

        renvoie :
        ---------
        res : list
        tableau des positions des reines par colonnes
        chaque valeur correspond au numéro de ligne
        l'indice correspond au numéro de colonne
        """
        progress = True
        res = [0 for _ in range(size)]
        # tant que le tableau n'est pas correct
        while progress:
            if is_valid(res):
                progress = False
            else:
                # incrémentation des valeurs
                res[0] = res[0]+1
                for i in range(0, size-1):
                    res[i+1] += res[i]//size
                    res[i] = res[i] % size
        return res

class Exchange(SolverRowList):
    def solve(size: int) -> Optional[list[int]]:
        """
        Créer une liste de valeur de 0 à size, 
        si la liste est bonne :
            - renvoie le résultat correcte
        sinon 
            - prend un indice aléatoire
            - échange les valeurs entre l'indice et l'indice au-dessus

        paramètre :
        -----------
        size : int
        nombre de reine

        renvoie :
        ---------
        res : list
        tableau des positions des reines par colonnes
        """
        res = [i for i in range(size)]
        while not is_valid(res):
            index = random.randint(0, size-1)
            res[index], res[(index+1) % size] = res[(index+1) % size], res[index]
        return res
