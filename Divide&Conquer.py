global A
global B
global C


def Kwalk(n, board):
    board[1] = 1
    for i in range(2, n):
        board[i] = (board[i-1]+2) % n
        if board[i] == 0:
            board[i] = n
    return


def Breakdown(n):
    global A
    global B
    global C

    A = 5
    M = n
    while ((M % 4) != 0):
        M = M-4
    C = n-M
    if (C % 3) == 0:
        M = M-4
        C = C+4
    B = M / 4

    return


def Setup(n, board):
    global A
    global B
    global C

    if C == 1:
        board[1] = 1
        bigboard = 1
    for i in range(C+1, n):
        j = i-C+B
        if (j % B) == 1:
            bigboard = (bigboard+2) % A
            if bigboard == 0:
                bigboard = 5
            board[i] = B * (bigboard-2) + 1 + C
        else:
            board[i] = (((board[i-1]+2) - C) % B) + (B*(bigboard-2)) + C
            if board[i] == ((B * (bigboard - 2)) + C):
                board[i] = board[i-1] + 2
    return


def Shift(n, board):
    n = n-1
    for i in range(1, n):
        board[i] = board[i+1]-1
    return


def Output(board):
    for i in range(1, n):
        print(board[i], end=' ')
    return


# programme principal
if __name__ == '__main__':
    n = 4
    max = 100
    board = [0]*max
    A = 0
    B = 0
    C = 0

    for number in range(1, max):
        n = number
        if (n % 2 == 0):
            n += 1
            even = True
        else:
            even = False
        if ((n == 3) or (n == 9) or (n == 15) or (n == 27) or (n == 39)):
            print("pas de solution", end='')
        else:
            if n % 3 != 0:
                Kwalk(n, board)
            else:
                Breakdown(n)
                Setup(n, board)
            if even:
                Shift(n, board)
                Output(board)
