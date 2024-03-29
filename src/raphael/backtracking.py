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
        is_row_free, is_column_free = [
            [True for _ in range(board.n)] for _ in range(2)]

        is_diag_neso_free, is_diag_nose_free = [
            [True for _ in range(board.n * 2 - 1)] for _ in range(2)]

        def diag_neso_index(row: int, col: int) -> int:
            return row + board.n - col - 1

        def diag_nose_index(row: int, col: int) -> int:
            return row + col

        def possible(row: int, col: int) -> bool:
            return is_row_free[row]\
                and is_column_free[col]\
                and is_diag_neso_free[diag_neso_index(row, col)]\
                and is_diag_nose_free[diag_nose_index(row, col)]

        def set_possible(row: int, col: int, is_possible: bool):
            is_row_free[row] = is_possible
            is_column_free[col] = is_possible
            is_diag_neso_free[diag_neso_index(row, col)] = is_possible
            is_diag_nose_free[diag_nose_index(row, col)] = is_possible

        nb_queens_remaining = board.n

        def backtracking_rec(cell_i: int) -> bool:
            nonlocal nb_queens_remaining

            if cell_i == n ** 2:
                return nb_queens_remaining == 0

            row, col = cell_i // n, cell_i % n
            if possible(row, col):
                # Assuming that we place our queen here
                set_possible(row, col, False)
                nb_queens_remaining -= 1

                # move on to the next cell: recursive call to see if the queen positions is good afterwards
                if (backtracking_rec(cell_i + 1)):
                    # the queen position is good, place it here
                    board[row, col] = False
                    return True

                nb_queens_remaining += 1
                # placing the subsequent queens assuming there's a queen here as failed, revert
                set_possible(row, col, True)

            # move on to next cell
            return backtracking_rec(cell_i + 1)

        if backtracking_rec(0):
            return board
        else:
            return None

    @staticmethod
    def to_board(n: int, solution: Board) -> Board:
        return solution
