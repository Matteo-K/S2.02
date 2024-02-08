# Backtracking

> Comment identifier les diagonales ?

On se base sur leur centre.

How do identify diagonals and find which diagonal a specific cell belong to ?

Example : in n=4 board, the cell at (0,1) belong to NE-SO #2 and NO-SE #1.

NE-SO:

0. 3
1. 2
2. 1
3. 0

4. 4
5. 3
6. 2
7. 1

8. 5
9. 4 = 2 + (4 - 1 - 1)
10. 3
11. 2

12. 6 = 3 + (4 - 0 - 1) = 3 + 3
13. 5 = 3 + (4 - 1 - 1) = 3 + 1
14. 4 = 3 + (4 - 2 - 1) = 3 + 2
15. 3

$$
\begin{split}&\lfloor\frac{tileNo}{N}\rfloor + N - tileNo  \mod N - 1\\
\Leftrightarrow\ &row + N - col - 1\end{split}
$$

NO-SE:

0. 0
1. 1
2. 2
3. 3

4. 1
5. 2
6. 3
7. 4

8. 2 = 2 + 0
9. 3 = 2 + 1
10. 4 = 2 + 2
11. 5 = 2 + 3

12. 3 = 3 + 0
13. 4 = 3 + 1
14. 5 = 3 + 2
15. 6 = 3 + 3

$$
\begin{split}
&\lfloor\frac{tileNo}{N}\rfloor + tileNo \mod N\\
\Leftrightarrow\ &row + col
\end{split}
$$
