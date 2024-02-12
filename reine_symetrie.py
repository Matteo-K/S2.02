N = 8

[0, 0, 0, 0, 4, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 3, 0, 0]
[0, 2, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 2, 0]
[0, 0, 3, 0, 0, 0, 0, 0]
[0, 0, 0,
 0, 0, 0, 0, 1]
[0, 0, 0, 4, 0, 0, 0, 0]


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
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][1] - queens[j][1]) == abs(queens[i][0] - queens[j][0]):
                return False
    return True


def main():
    affiche_echiquier(echiquier)
    queens = []
    print("donne la ligne")
    x = int(input())
    print("donne la colonne")
    y = int(input())
    queens.append([x, y])
    queens.append([N-1-x, N-1-y])
    indice_ligne = 0
    indice_colonne = 0
    for indice_colonne in range(4):
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


print("")
affiche_echiquier(echiquier)

main()
