#!/bin/env python3

from typing import Iterable, Callable, TypeVar, Optional
from board import Board

T = TypeVar('T')

def firstOrNone(iterable: Iterable[T], delegate: Callable[[T], bool]) -> Optional[T]:
    return next((i for i in iterable if delegate(i)), None)

def solve(board: Board):
    """ Cet algoritmhe de backtracking utilise un graphe implicite (prenant la forme d'un arbre de décision), et des contraintes pour parcourir cet arbre pour arriver une solution valide. """
    def diag_ne_so(r: int, c: int) -> tuple[int, int]:
        a = r + c
        dc = min(a, board.n - 1)
        dr = a - dc
        return dr, dc

    def diag_no_se(r: int, c: int) -> tuple[int, int]:
        m = min(r, c)
        return r - m, c - m

#    for r in range(0, board.n):
#        for c in range(0, board.n):
#            print((r,c), diag_no_se(r, c))

    solution: list[int] = []

    def in_solution(r: int, c: int) -> bool:
        return len(solution) > c and solution[c] == r

    def can_place_at(r: int, c: int) -> bool:
        if r in solution:
            return False
        
        # NE SO
        dr, dc = diag_ne_so(r, c)
        print('ne of', (r, c), 'is', (dr, dc))
        while dr < board.n and dc > 0:
            print(dr, dc, flush=True)
            if in_solution(dr, dc):
                print('fail ne_so')
                return False
            dr += 1
            dc -= 1

        # NO SE
        dr, dc = diag_no_se(r, c)
        print('no of', (r, c), 'is', (dr, dc))
        while dr < board.n and dc < board.n:
            if in_solution(dr, dc):
                print('fail no_se')
                return False
            dr += 1
            dc += 1

        return True

    
    for c in range(0, board.n):
        r = firstOrNone(range(0, board.n), lambda r: can_place_at(r, c))
        if r is None:
            c -= 1
        else:
            print("PUT", (r, c))
            solution.append(r)
            board[r, c] = False

    return True