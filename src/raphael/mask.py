"""
Algorithme de masque
"""

from src.solver import SolverRowList
from typing import Optional


class Mask(SolverRowList):
    @staticmethod
    def solve(n: int) -> Optional[SolverRowList]:
        nbo_queens_threatening_cell_at = [[0 for _ in range(n)] for _ in range(n)]

        def diag_no_se(r: int, c: int) -> tuple[int, int]:
            m = min(r, c)
            return r - m, c - m

        def diag_ne_so(r: int, c: int) -> tuple[int, int]:
            a = r + c
            dc = min(a, n - 1)
            dr = a - dc
            return dr, dc

        def mask(delta: int, row: int, column: int):
            for i in range(n):
                # column
                nbo_queens_threatening_cell_at[i][column] += delta
                # row
                nbo_queens_threatening_cell_at[row][i] += delta

            # diag NO SE
            dr, dc = diag_no_se(row, column)
            while dr < n and dc < n:
                nbo_queens_threatening_cell_at[dr][dc] += delta
                dr += 1
                dc += 1

            # diag NE SO
            dr, dc = diag_ne_so(row, column)
            while dr < n and dc >= 0:
                nbo_queens_threatening_cell_at[dr][dc] += delta
                dr += 1
                dc -= 1

        solution = [None for _ in range(n)]

        def backtrack(foundCount: int) -> bool:
            if foundCount == n:
                # the solution is complete
                return True

            # Solve columns by pitching away from n//2 as foundCount increases.
            # Example for n=4: 1, 2, 0, 3
            if foundCount % 2 == 0:
                column = n // 2 - foundCount // 2 - 1
            else:
                column = n // 2 + foundCount // 2

            validRows = (r for r in range(n) if nbo_queens_threatening_cell_at[r][column] == 0)
            for validRow in validRows:
                mask(1, validRow, column)
                if backtrack(foundCount + 1):
                    solution[column] = validRow
                    return True
                else:
                    mask(-1, validRow, column)

            return False

        if backtrack(0):
            assert None not in solution
            return solution
        else:
            return None
