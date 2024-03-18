# "reine_symetrie" est une supposition que j'ai fait apres avoir remarqué qu'il y avait plusieurs solutions au problème des reines
# j'ai donc essayé de faire un programme mais il n'a pas marché et j'ai remarqué qu'il y avait beaucoup de cas qui ne permettait pas de resoudre
# le probleme (ex: quand on pose les reines successivement elles finnissent par se bloqpuen entre elles)

N = 8


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
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][1] - queens[j][1]) == abs(queens[i][0] - queens[j][0]):
                return False
    return True

#


[
    [0, 0, 3, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 3, 0, 0]
]


def main():
    affiche_echiquier(echiquier)
    queens = []  # position des reines

    # # demande de poser une reine
    # print("donne la ligne")
    # x = int(input())
    # print("donne la colonne")
    # y = int(input())
    # queens.append([x, y])
    # queens.append([N-1-x, N-1-y])

    indice_ligne = 0
    indice_colonne = 0
    for indice_colonne in range(N/2):
        modif = False
        indice_ligne = 0

        print(indice_colonne)
        while indice_ligne < N and modif == False:

            queens.append([indice_ligne, indice_colonne])
            queens.append([N-indice_ligne-1, N-indice_colonne-1])
            if is_valid(queens):
                modif = True

            else:
                queens = queens[:-2]
                indice_ligne += 1
            print(queens)
    for i in range(N):

        a = queens[i][0]
        b = queens[i][1]
        echiquier[a][b] = 1


def main():
    affiche_echiquier(echiquier)
    queens = []  # position des reines

    # # demande de poser une reine
    # print("donne la ligne")
    # x = int(input())
    # print("donne la colonne")
    # y = int(input())
    # queens.append([x, y])
    # queens.append([N-1-x, N-1-y])

    indice_ligne = 0
    indice_colonne = 0
    for indice_colonne in range(N/2):
        modif = False
        indice_ligne = 0

        print(indice_colonne)
        while indice_ligne < N and modif == False:

            queens.append([indice_ligne, indice_colonne])
            queens.append([N-indice_ligne-1, N-indice_colonne-1])
            if is_valid(queens):
                modif = True

            else:
                queens = queens[:-2]
                indice_ligne += 1
            print(queens)
    for i in range(N):

        a = queens[i][0]
        b = queens[i][1]
        echiquier[a][b] = 1


def main2():
    affiche_echiquier(echiquier)
    queens = []  # position des reines

    indice_ligne = 0
    indice_colonne = 0
    while not is_valid(queens) and len(queens) < N:

        indice_ligne = 0
        while not is_valid(queens) and indice_ligne < N:
            queens.append[indice_ligne][indice_colonne]
            queens.append[N-1-indice_ligne][N-1-indice_colonne]
            if not is_valid(queens):
                queens = queens[:-2]
                indice_ligne += 1

        if indice_ligne >= N:
            indice_colonne -= 1
        else:
            indice_colonne += 1

    for i in range(N):

        a = queens[i][0]
        b = queens[i][1]
        echiquier[a][b] = 1


print("")
affiche_echiquier(echiquier)

main2()
