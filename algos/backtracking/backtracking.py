from board import Board

def backtracking(board: Board) -> bool:
    """ Algorithme de backtracking: place board.n reines """
    isRowFree, isColumnFree = [[True for _ in range(board.n)] for _ in range(2)]
    # NE-SO : 0 NE, n-1 SO
    # NO-SE : 0 NO, n-1 SE
    isDiagNeSoFree, isDiagNoSeFree = [
        [True for _ in range(board.n * 2 - 1)] for _ in range(2)]

    def diagNeSoIndex(row: int, col: int) -> int:
        return row + board.n - col - 1

    def diagNoSeIndex(row: int, col: int) -> int:
        return row + col

    def possible(row: int, col: int) -> bool:
        return isRowFree[row] and isColumnFree[col] and isDiagNeSoFree[diagNeSoIndex(row, col)] and isDiagNoSeFree[diagNoSeIndex(row, col)]

    def setPossible(row: int, col: int, isPossible: bool):
        isRowFree[row] = isPossible
        isColumnFree[col] = isPossible
        isDiagNeSoFree[diagNeSoIndex(row, col)] = isPossible
        isDiagNoSeFree[diagNoSeIndex(row, col)] = isPossible

    nbQueensRemaining = board.n

    def backtracking_rec(tileNo: int) -> bool:
        nonlocal nbQueensRemaining

        if tileNo == board.n * board.n:
            return nbQueensRemaining == 0

        row = tileNo // board.n
        col = tileNo % board.n

        if possible(row, col):
            # Assuming that we place our queen here
            setPossible(row, col, False)
            nbQueensRemaining -= 1

            # move on to the next cell: recursive call to see if the queen positions is good afterward
            if (backtracking_rec(tileNo + 1)):
                # the queen position is good, place it here
                board[row, col] = False
                return True

            nbQueensRemaining += 1
            # placing the subsequent queens assuming there's a queen here as failed, revert
            setPossible(row, col, True)

        # move on to next cell
        return backtracking_rec(tileNo + 1)

    return backtracking_rec(0)


if __name__ == '__main__':
    # True indique que la case est libre
    board = Board(8)
    print(backtracking(board))
    # Afficher la solution
    print(board)
