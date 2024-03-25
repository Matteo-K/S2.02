from abc import ABC, abstractstaticmethod
from typing import Any
from src.board import Board
from typing import Optional


class Solver(ABC):
    """ Interface for a N-Queen solver algorithm. """
    @abstractstaticmethod
    def solve(n: int) -> Optional[Any]:
        """ Solves the N-Queen problem.
            n: number of queens.
            Returns: the solution, of any type, or None, if no solution was found. The return value should be printable."""

    @abstractstaticmethod
    def to_board(n: int, solution: Any) -> Board:
        """ Converts the solution to a board for easier visualization. """


class SolverRowList(Solver):
    """ Interface for a N-Queen solver algorithm that returs a list of rows where to place to the queens on the board. """
    @abstractstaticmethod
    def solve(n: int) -> Optional[list[int]]:
        """ Solves the N-Queen problem.
            n: number of queens.
            Returns: the solution, as a list of integers where the indices are the columns and the values are the rows for each queen on the board, or None, if no solution was found.
        """

    @staticmethod
    def to_board(n: int, solution: list[int]) -> Board:
        board = Board(n)
        assert len(solution) == n
        for c, r in enumerate(solution):
            board[c, r] = False
        return board
