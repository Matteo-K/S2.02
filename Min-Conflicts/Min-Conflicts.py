from colorama import Fore, Back, Style
n=8

board = [[0 for i in range(n)] for i in range(n)]

listeR = [(i+7)%8 for i in range(n)]
print(listeR)

for i in range(0,n):
    board[listeR[i]][i]=8

def afficher(echequier):
    taille = len(echequier)
    for i in echequier:
        for j in i:
            if j==8:
                print(Fore.RED + str(j) + "  ", end ="")
                print(Style.RESET_ALL, end="")
            else:
                print (str(j) + "  ", end ="")
        print()

afficher(board)