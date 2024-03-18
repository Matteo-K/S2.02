from colorama import Fore, Back, Style
from random import *
n=8

board = [[0 for i in range(n)] for i in range(n)]

listeR = [randint(0,7)]+[None for i in range(n-1)]


print(listeR)

for i in range(0,n):
    if listeR[i] is not None:
        board[listeR[i]][i]=8

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

afficher(board)

def conflicts(listeR):
    #fonction renvoi tableau des conflits
    board = [[0 for i in range(n)] for i in range(n)]
    for ind in range(len(listeR)):
        r=listeR[ind]
        print(r)
        if r!= None:
            for i in range(n):
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

def place(indice, board):
    taille = len(board)
    min = 999
    indiceMin = None
    for i in range(taille):
        if board[i][indice] < min:
            min = board[i][indice]
            indiceMin = i





afficher(conflicts(listeR))