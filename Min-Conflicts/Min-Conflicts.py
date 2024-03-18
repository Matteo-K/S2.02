from colorama import Fore, Back, Style
from random import *

def afficher(echequier):
    taille = len(echequier)
    for i in echequier:
        for j in i:
            if j!=0:
                print(Fore.RED + str(j) + "  ", end ="")
                print(Style.RESET_ALL, end="")
            else:
                print (str(j) + "  ", end ="")
        print()


def conflicts(listeR):
    #fonction renvoi tableau des conflits
    board = [[0 for i in range(n)] for i in range(n)]
    for ind in range(len(listeR)):
        r=listeR[ind]
        if r!= None:
            for i in range(n):
                # la case ou est mise la reine n'est pas en conflit
                if (i!=ind):
                    board[r][i]+=1

            #diagonale vers le bas
            for i in range(n):
                diag = r+i-ind
                if (diag < n) and (i!=ind):
                    if diag > -1:
                        board[diag][i]+=1 
            #diagonale vers le haut
            for i in range(n):
                diag = (r-i+ind)%n
                if ((r-i+ind) < n) and (i!=ind):
                    if (r-i+ind) > -1:
                        board[diag][i]+=1
   
    return board

# fonction pour placer une reine dans la case d'une colonne avec le moins de conflits
# fonction renvoie la ligne du placement de la reine 
# prend en paramètre l'indice de la colonne et le tableau des conflits
def place(indice, board):
    taille = len(board)
    min = 999
    indiceMin = []
    for i in range(taille):
        if board[i][indice] < min:
            min = board[i][indice]
            indiceMin=[]
            indiceMin.append(i)
        elif board[i][indice] ==  min:
            indiceMin.append(i)
    return choice(indiceMin)

def valide(tableauConf, coordsReines):
    res = True
    taille = len(coordsReines)
    i = 0
    while (res)and(i<taille):
        if tableauConf[coordsReines[i]][i] != 0:
            res=False
        i+=1
    return res

n=8
fin=False
board = [[0 for i in range(n)] for i in range(n)]
listeR = [None for i in range(n)]

while not fin:
    #initialisation
    listeR = [None for i in range(n)]

    confBoard= conflicts(listeR)
    for i in range(n):
        res = place(i, confBoard)
        listeR[i]=res
        confBoard= conflicts(listeR)
    
    fin = valide(confBoard, listeR)


print(listeR)
afficher(confBoard)

#place les reines sur un echequier normal
for i in range(0,n):
    if listeR[i] is not None:
        board[listeR[i]][i]=8

print()
afficher(board)