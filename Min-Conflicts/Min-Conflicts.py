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
    board = [[0 for i in range(n)] for i in range(n)]
    for r in listeR:
        print(r)
        if r!= None:
            for i in range(9):
                print("ee")
    return board

def place(indice, board):
    taille = len(board)
    min = 999
    indiceMin = None
    for i in range(taille):
        if board[i][indice] < min:
            min = board[i][indice]
            indiceMin = i
