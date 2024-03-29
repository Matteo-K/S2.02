"""
Algorithme de backtracking
"""

from src.solver import Solver
from src.board import Board
from typing import Optional


class Backtracking(Solver):
    @staticmethod
    def solve(n: int) -> Optional[Board]:
        board = Board(n)
        isRowFree, isColumnFree = [
            [True for _ in range(board.n)] for _ in range(2)]
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

        def backtracking_rec(cell_i: int) -> bool:
            nonlocal nbQueensRemaining

            if cell_i == n ** 2:
                return nbQueensRemaining == 0

            row, col = cell_i // n, cell_i % n
            if possible(row, col):
                # Assuming that we place our queen here
                setPossible(row, col, False)
                nbQueensRemaining -= 1

                # move on to the next cell: recursive call to see if the queen positions is good afterwards
                if (backtracking_rec(cell_i + 1)):
                    # the queen position is good, place it here
                    board[row, col] = False
                    return True

                nbQueensRemaining += 1
                # placing the subsequent queens assuming there's a queen here as failed, revert
                setPossible(row, col, True)

            # move on to next cell
            return backtracking_rec(cell_i + 1)

        if backtracking_rec(0):
            return board
        else:
            return None

    @staticmethod
    def to_board(n: int, solution: Board) -> Board:
        return solution
