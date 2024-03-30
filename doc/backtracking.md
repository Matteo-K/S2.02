# Algorithme de backtracking

Backtracking simple avec une optimisation : au lieu de parcourir les lignes, colonnes et diagonales sur la grille, on stocke si elle sont libres dans des listes annexes.

Cela permet de réduire le nombre d'accès en mémoire à réaliser pour déterminer si on peut placer une reine.

> Comment identifier les diagonales et trouver les diagonales d'une case ?

On se base sur leur centre.

Et donc l'indice de chaque diagonale de la liste des donné ainsi:

$$
\begin{split}
d_{NE\\\_SO} &= \lfloor\frac{tileNo}{N}\rfloor + N - tileNo \mod N - 1\\
d_{NE\\\_SO} &= row + N - col - 1
\end{split}
$$

$$
\begin{split}
d_{NO\\\_SE} &= \lfloor\frac{tileNo}{N}\rfloor + tileNo \mod N\\
d_{NO\\\_SE} &= row + col
\end{split}
$$

## Benchmark

```mermaid
xychart-beta
title "Temps CPU - backtracking (100 essais)"
x-axis "N" 4 --> 14
y-axis "Temps CPU (ms)"
line "backtracking moyenne" [0.15929386999999962, 0.07978077000000083, 2.4447990700000055, 0.23289553999999657, 19.460690309999997, 6.710828330000007, 39.981004200000044, 20.828582560000058, 277.5929147099997, 118.65195076999989, 8397.61691225]
```

```mermaid
xychart-beta
title "Mémoire - backtracking (100 essais)"
x-axis "N" 4 --> 14
y-axis "Mémoire (octets)"
line "backtracking moyenne" [2348.22, 2586.4, 2716.69, 2771.12, 2870.64, 3879.2, 4057.44, 4243.84, 4440.8, 4760.56, 4958.49]
```
