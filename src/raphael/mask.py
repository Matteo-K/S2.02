"""
Algorithme de masque
"""

from src.solver import SolverRowList
from typing import Optional, Sequence
from array import array


class Mask(SolverRowList):
    @staticmethod
    def solve(n: int) -> Optional[Sequence[int]]:
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

        # Since the columns aren't solve lineraly, we need to create the whole list before starting.
        # -1 is used as a placeholder value until a solution is found
        solution = array('i', (i for i in range(n)))

        def backtrack(found_count: int) -> bool:
            if found_count == n:
                # the solution is complete
                return True

            # Solve columns by pitching away from n//2 as found_count increases.
            if found_count % 2 == 0:
                column = n // 2 - found_count // 2 - 1
            else:
                column = n // 2 + found_count // 2

            valid_rows = (r for r in range(n) if nbo_queens_threatening_cell_at[r][column] == 0)
            for valid_row in valid_rows:
                mask(1, valid_row, column)
                if backtrack(found_count + 1):
                    solution[column] = valid_row
                    return True
                else:
                    mask(-1, valid_row, column)

            return False

        if backtrack(0):
            assert -1 not in solution
            return solution
        else:
            return None
