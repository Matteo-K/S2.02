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

## Optimisaton 1 : spirale

Voir <mask.md>, faisons des spirales vers l'extérieur.

D'abord trouvons une fonction pour obtenir les coordonnées de la prochaine case à partire de `tileNo`:

&nbsp;|0|1|2|3
-|-|-|-|-
**0**|0|1|2|3
**1**|4|5|6|7
**2**|8|9|10|11
**3**|12|13|14|15

&nbsp;|0|1|2|3|4
-|-|-|-|-|-
**0**|0|1|2|3|4
**1**|5|6|7|8|9
**2**|10|11|12|13|14
**3**|15|16|17|18|19
**4**|20|21|22|23|24

On voudrait 5, 6, 10, 9, 8, 4, 0, 1, 2, 3, 7, 11 ,15, 14, 13, 12

ou 1:1, 1:2, 2:2, 2:1, 2:0, 1:0, 0:0, 0:1, 0:2, 0:3, 1:3, 2:3, 3:3, 3:2, 3:1, 3:0

on pourrait faire un générateur qui part de `n//2`:`n//2`

nope that doesn't work, it makes performance much worth, i guess i stand corrected.
