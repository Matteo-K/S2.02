SIZE = 4

grid = [[0, 1, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0]]


def possible(grid, l, c):
    for line in range(SIZE):
        for column in range(SIZE):
            if (possibleLine(grid, line) and possibleColumn(grid, column) and possibleDiag(grid, line, column)) == True:
                print(line, column)


def possibleLine(grid, l):
    for column in range(SIZE):
        if (grid[l][column] == 1):
            return False
    return True


def possibleColumn(grid, c):
    for line in range(SIZE):
        if (grid[line][c] == 1):
            return False
    return True


def possibleDiag(grid, l, c):
    # Vérifier la diagonale supérieure gauche
    for i, j in zip(range(l-1, -1, -1), range(c-1, -1, -1)):
        if grid[i][j] == 1:
            return False

    # Vérifier la diagonale supérieure droite
    for i, j in zip(range(l-1, -1, -1), range(c+1, len(grid))):
        if grid[i][j] == 1:
            return False

    # Vérifier la diagonale inférieure gauche
    for i, j in zip(range(l+1, len(grid)), range(c-1, -1, -1)):
        if grid[i][j] == 1:
            return False

    # Vérifier la diagonale inférieure droite
    for i, j in zip(range(l+1, len(grid)), range(c+1, len(grid))):
        if grid[i][j] == 1:
            return False

    return True
