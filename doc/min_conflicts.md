# Algorithme des conflits minimum

## Principe

Le principe de cet algorithme repose sur une notation des cases en danger et le choix aléatoire de placement de reine, c'est un algorithme glouton.

## Explications

L'algorithme de min conflits consite a placer une première reine, de manière aléatoire, sur la première colonne d'un échiquier vide, et on note toutes les cases mises en danger par cette reine.
Puis quand on place la deuxieme reine dans la deuxième colonne on prend on compte les cases mises en danger et on place cette nouvelle reine dans une des cases mise le moins en danger, puis on note encoretoutes les cases mises en danger en augmantant la sévérité du danger des cases déja en danger. On continue cette approche jusqu'à que toutes les reines soient placées.

Le fonctionnement de cette algorithme repose sur l'aléatoire du placement des reines pour éviter les blockages. Cela fait que chaque solution est quasi-unique et donc non-déterministe.

## Benchmark

```mermaid
xychart-beta
title "Temps CPU - min_conflicts (100 essais)"
x-axis "N" 4 --> 20
y-axis "Temps CPU (ms)"
line "min_conflicts moyenne" [0.2277152300000007, 0.26142849999999995, 4.327412469999998, 1.274545629999999, 4.132404469999985, 5.705930550000011, 14.780794059999987, 22.845388259999968, 37.43899378999998, 43.24423219000001, 58.39806439000006, 81.73474827000024, 107.3758931900002, 145.80460150999983, 219.7472962200006, 241.4144685000005, 279.6485111700009]
```

```mermaid
xychart-beta
title "Mémoire - min_conflicts (100 essais)"
x-axis "N" 4 --> 20
y-axis "Mémoire (octets)"
line "min_conflicts moyenne" [882.48, 1297.82, 1453.42, 1581.84, 1710.96, 3120.08, 3441.2, 3698.32, 3955.44, 4212.56, 4472.53, 4726.8, 4983.92, 7545.04, 7994.16, 8379.28, 8764.4]
```
