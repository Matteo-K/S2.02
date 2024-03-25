"""
Fonctions annexes à la résolution
"""


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
