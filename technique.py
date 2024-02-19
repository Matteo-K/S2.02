import time
import random


def is_valid(queens: list[int]) -> bool:
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
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == j - i:
                return False
    return True


def solverRandom(size: int) -> list[int]:
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
    tableau des positions des reines pas colonnes
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

def forcing(size):
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
    tableau des positions des reines pas colonnes
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