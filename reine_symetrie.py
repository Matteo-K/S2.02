N = 8

[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
morphes, av
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 1, 0, 0, 0, 0]


[0, 0, 0, 0, 1, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 1, 0, 0, 0, 0]


# création d'un echicquier ou les case du haut (en ligne 8) contiennent des reines
# les 0 représentes des cases vides
# les 1 representes les reines
echiquier = []
for i in range(N):
    echiquier.append([])
    for j in range(N):
        echiquier[i].append(0)


def affiche_echiquier(ech):
    for i in range(N):
        print(ech[i])
    print("\n")


def is_valid(queens: list) -> bool:
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


def main():
    affiche_echiquier(echiquier)
    modif = False
    i = 0
    indice_ligne = 0
    indice_colonne = 0
    for indice_colonne in range(4):
        modif = False
        indice_ligne = 0
        while indice_ligne < N and modif == False:
            echiquier[N-indice_ligne-1][N-indice_colonne-1] = 1
            if possible(echiquier, indice_ligne, indice_ligne):
                echiquier[indice_ligne][indice_colonne] = 1
                modif = True

            else:
                echiquier[N-indice_ligne-1][N-indice_colonne-1] = 0
                indice_ligne += 1
        print("")
        affiche_echiquier(echiquier)
        print(indice_colonne)


main()
