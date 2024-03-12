#!/bin/env python3

from typing import Iterable, Callable, TypeVar, Optional
from board import Board
from solver import Solver

T = TypeVar('T')


def firstOrNone(iterable: Iterable[T], delegate: Callable[[T], bool]) -> Optional[T]:
    return next((i for i in iterable if delegate(i)), None)


class BacktrackingGraphe(Solver):
    @staticmethod
    def solve(n: int) -> Optional[list[int]]:
        """ Cet algoritmhe de backtracking utilise un graphe implicite (prenant la forme d'un arbre de décision), et des contraintes pour parcourir cet arbre pour arriver une solution valide.
        Retourne une solution sous la forme d'une liste de lignes"""
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
            while dr < n and dc > 0:
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

        def backtrack(partialSolution: list[int]) -> bool:
            column = len(solution)  # determine the next column to solve
            if len(partialSolution) == n:
                # the solution is complete
                return partialSolution

            validRows = [r for r in range(n) if can_place_at(
                partialSolution, r, column)]
            for validRow in validRows:
                partialSolution += [validRow]
                if backtrack(partialSolution):
                    return True
                else:
                    partialSolution.remove(validRow)

            return False

        solution = []
        # we must always find a solution
        if backtrack(solution):
            return solution
        else:
            return None

    @staticmethod
    def toBoard(n: int, solution: list[int]) -> Board:
        board = Board(n)
        assert len(solution) == n
        for c, r in enumerate(solution):
            board[c, r] = False
        return board
