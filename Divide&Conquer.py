def Kwalk(n, board):
   board[1]=1
   for i in range(2,n):
       board[i]= (board[i-1]+2)%n
       if board[i] == 0:
          board[i]=n
   return

def Breakdown(n, A, B, C):
    A=5
    M=n
    while (M%4 != 0):
        M = M-4
    C = n-M
    if C%3==0:
        M=M-4
        C=C-4
    B= M / 4
    return

def Setup (n, A, B, C, board):
    if C==1:
        board[1]=1
        bigboard = 1
        for i in range(C+1,n):
            j = i-C+B
            if j%B ==1:
                bigboard= (bigboard+2) % A
                if bigboard==0:
                    bigboard = 5
                    board[i] = B * (bigboard-2) + 1 + C 

                else:
                    board[i] = (((board[i-1]+2) - C) % B)+ (B*(bigboard-2))+ C
                    if board[i] == ((B * (bigboard - 2)) + C):
                        board[i] = board[i-1] + 2
    return

def Shift(n, board):
    n=n-1
    for i in range (1,n):
        board[i] = board[i+1]-1
    return    
def Output(board):
    for i in range(1,n):
        print(board[i], end=' ')
    return
#programme principal
n=4
max=100
board=[0]*100
A=None
B=None
C=None

for number in range(max):
    n=number
    if (n%2 == 0):
        n+=1
        even=True
    else:
        even = False
    if ((n==3) or (n==9) or (n==15) or (n==27) or (n==39)):
        print("pas de solution",end='')
    else:
        if n%3 != 0:
            Kwalk(n,board)
        else:
            Breakdown(n,A,B,C)
            Setup(N,A,B,C,board)
        if even:
            Shift(n,board)
            Output(board)
