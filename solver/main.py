#!/bin/env python3


from board import Board
import backtracking, backtracking_graphe

if __name__ == '__main__':
    board = Board(8)
    print(backtracking_graphe.solve(board))
    print(board)
