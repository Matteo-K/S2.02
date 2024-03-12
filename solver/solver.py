from abc import ABC, abstractstaticmethod
from typing import Any
from board import Board
from typing import Optional

class Solver(ABC):
    """ Interface for a N-Queen solver algorithm. """
    @abstractstaticmethod
    def solve(n: int) -> Optional[Any]:
        """ Solves the N-Queen problem.
            n: number of queens.
            Returns: the solution, of any type, or None, if no solution was found. The return value should be printable."""

    @abstractstaticmethod
    def toBoard(solution: Any) -> Board:
        """ Converts the solution to a board for easier visualization. """
