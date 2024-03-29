"""
Algorithme de backtracking graphe
"""

from typing import Iterable, Callable, TypeVar, Optional
from src.board import Board
from src.solver import Solver

T = TypeVar('T')


def firstOrNone(iterable: Iterable[T], predicate: Callable[[T], bool]) -> Optional[T]:
    return next((i for i in iterable if predicate(i)), None)


class BacktrackingGraphe(Solver):
    @staticmethod
    def solve(n: int) -> Optional[list[int]]:
        """ Cet algoritmhe de backtracking utilise un graphe implicite (prenant la forme d'un arbre de décision), et des contraintes pour parcourir cet arbre pour arriver une solution valide.
        Retourne une solution sous la forme d'une liste de lignes."""
        def diag_ne_so(r: int, c: int) -> tuple[int, int]:
            a = r + c
            dc = min(a, n - 1)
            dr = a - dc
            return dr, dc

        def diag_no_se(r: int, c: int) -> tuple[int, int]:
            m = min(r, c)
            return r - m, c - m

        def in_solution(solution: list[int], r: int, c: int) -> bool:
            return len(solution) > c and solution[c] == r

        def can_place_at(solution: list[int], r: int, c: int) -> bool:
            if r in solution:
                return False

            # NE SO
            dr, dc = diag_ne_so(r, c)
            while dr < n and dc >= 0:
                if in_solution(solution, dr, dc):
                    return False
                dr += 1
                dc -= 1

            # NO SE
            dr, dc = diag_no_se(r, c)
            while dr < n and dc < n:
                if in_solution(solution, dr, dc):
                    return False
                dr += 1
                dc += 1

            return True

        def backtrack(partial_solution: list[int]) -> bool:
            column = len(solution)  # determine the next column to solve
            if len(partial_solution) == n:
                # the solution is complete
                return partial_solution

            valid_rows = (r for r in range(n) if can_place_at(
                partial_solution, r, column))
            for valid_row in valid_rows:
                partial_solution.append(valid_row)
                if backtrack(partial_solution):
                    return True
                else:
                    partial_solution.remove(valid_row)

            return False

        solution = []

        if backtrack(solution):
            return solution
        else:
            return None

    @staticmethod
    def to_board(n: int, solution: list[int]) -> Board:
        board = Board(n)
        assert len(solution) == n
        for c, r in enumerate(solution):
            board[c, r] = False
        return board
