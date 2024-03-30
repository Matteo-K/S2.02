# Algorithme de symétrie

L'algorithme symétrie est un algorithme back-tracking cependant Les reines sont posées 2 par deux symétriquement.
Il est rapide et demande peu de mémoire cependant dans certains cas il va prendre beaucoup de temps comme quand l'échiquier à un côté de 32 cases.

## Fonction is_valid_clg

La fonction is_valid_clg utilise une liste de coordonnées sous forme de liste à 2 dimensions pour la vérification
Il suffit de vérifier si deux points sur une même ligne.

Et de comparer qu'une reine n'est pas dans la diagonale d'une autre.
Pour cela, il suffit de comparer la différence verticale et la différence horizontale entre deux reines.
Si une reine est dans la diagonale d'une autre reine alors les deux résultats seront identiques.

## Benchmark

```mermaid
xychart-beta
title "Temps CPU - symetrie (100 essais)"
x-axis "N" 4 --> 26
y-axis "Temps CPU (ms)"
line "symetrie moyenne" [0.03888436999999745, 0.07079729000000423, 0.09813369000000016, 0.12040589000000212, 1.1114268100000002, 0.3258769600000033, 0.40480083000000056, 0.8828791400000024, 0.7432176800000023, 8.70280078, 73.31702786999993, 3.227480889999974, 2.092086970000011, 4.23314710000005, 3.1664858400000284, 33.658170329999976, 614.2566636600002, 52.80949120999978, 6.659513470000036, 21.751575200000843, 9.363117849999583, 19.470966069999776, 1147.1391551600013]
```

```mermaid
xychart-beta
title "Mémoire - symetrie (100 essais)"
x-axis "N" 4 --> 26
y-axis "Mémoire (octets)"
line "symetrie moyenne" [668.72, 728.15, 797.44, 901.44, 973.44, 1077.44, 1149.44, 1221.44, 1293.44, 1397.44, 1472.35, 1541.44, 1613.44, 1717.44, 1789.44, 1861.44, 1933.44, 2053.44, 2125.44, 2213.44, 2285.44, 2405.44, 2477.44]
```
