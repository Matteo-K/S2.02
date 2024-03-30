# Algorithme du ping-pong

(comme force brute mais avec de l'aléatoire)

Incrémente de 1 chaque indice du tableau de résultat

Quand le premier élément arrive à la limite n.
On réalise un modulo de n et incrémente de 1 au second élément et ainsi de suite.

La  différence avec l'algorithme fore brute c'est qu'ici on choisit la colonne à incrémenter aléatoirement

## Fonction is_valid

L'utilisation d'un tableau en 1 dimension valorise la vérification du tableau.
Il suffit de vérifier si deux points sur une même ligne.

Et de comparer qu'une reine n'est pas dans la diagonale d'une autre.
Pour cela, il suffit de comparer la différence verticale et la différence horizontale entre deux reines.
Si une reine est dans la diagonale d'une autre reine alors les deux résultats seront identiques.

## Benchmark

```mermaid
xychart-beta
title "Temps CPU - pingpong (100 essais)"
x-axis "N" 4 --> 9
y-axis "Temps CPU (ms)"
line "pingpong moyenne" [0.43158544999999937, 1.2264203100000048, 36.01595707999998, 85.68515811999998, 691.6693416500002, 5017.610365139998]
```

```mermaid
xychart-beta
title "Mémoire - pingpong (100 essais)"
x-axis "N" 4 --> 9
y-axis "Mémoire (octets)"
line "pingpong moyenne" [271.88, 256, 256, 256, 256, 320]
```
