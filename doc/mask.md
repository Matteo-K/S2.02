# Algorithme du masque

Idée initiale&nbsp;: au lieu d'utiliser des booléens pour indiquer si une cellule contient ou non une reine, on indique si une case est menacée ou non.

Donc quand on place un reine on met à faux la cellule de la reine, sa ligne et sa colonne, ainsi que ses deux diagonales.

Donc maintenant tout ce qu'il reste à faire c'est itérer sur les N premières cellules vraies.

On pourrait dire qu'on "masque" les cellules menacées lors de la résolution.

C'est une version optimisée du backtracking.

## Problème

Si le placement d'une reine menace une cellule, puis un second placement menace cette même cellule, alors quand une des deux reines est enlevée dans le backtracking, la cellule redeviendra sûre et on perdra l'information.

La solution est simplement d'utiliser des entiers à la place des booléens, c'est-à-dire que chaque cellule conserve le nombre de reines qui la menacent (0 au départ).

## Optimisation

Devrions-nous toujours commencer le backtracking à *0,0* (en haut à gauche). Il y a peut-être d'autres possibilités :

On pourrait commencer par le milieu et progresser vers l'extérieur en spirales dans le sens des aiguilles d'une montre.

Résultat : l'ordre des colonnes tangue de *n//2* vers *0* et *n-1*.

## Benchmark

```mermaid
xychart-beta
title "Temps CPU - mask (100 essais)"
x-axis "N" 4 --> 22
y-axis "Temps CPU (ms)"
line "mask moyenne" [0.10613521000000126, 0.0832255099999979, 0.42649796000000184, 0.2204729599999966, 0.24706734999999813, 0.32780015999999634, 1.0800761899999984, 0.5479058800000092, 2.8161100199999956, 9.037634949999996, 17.79152017, 4.898015949999981, 15.684820790000007, 31.94583832000001, 19.190213919999977, 53.86348665, 157.1056129000001, 614.0859673000008, 1220.90710111]
```

```mermaid
xychart-beta
title "Mémoire - mask (100 essais)"
x-axis "N" 4 --> 22
y-axis "Mémoire (octets)"
line "mask moyenne" [2542.32, 2801.04, 3094.24, 3413.28, 3692.96, 4676.8, 5047.92, 5382.48, 5798.24, 6131.12, 6532.21, 6896, 7328.96, 8787.28, 9260.88, 9698.64, 10096.08, 10578.64, 10976.08]
```
