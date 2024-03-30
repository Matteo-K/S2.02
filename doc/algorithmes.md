# S2.02 Sujet 2 - Algorithmes

**Principe** : on a un échiquier de N\*N cases, déterminer les agencements possibles de N reines.

**Contraintes** : une reine doit être unique dans sa ligne, sa colonne et sa diagonale.

## Approches algorithmiques

Il existe plusieurs types d'algorithmes traitant du problème des N reines pour un échiquier de côté N :

- Obtenir une solution
- Obtenir toutes les solutions
- Obtenir le nombre de solutions existantes

Nous avons choisi de nous focaliser sur des algorithmes qui permettent d'obtenir une solution.

Algorithme|Principe|Script
-|-|-
[Backtracking](backtracking.md)|Résolution case par case avec retour arrière|[backtracking.py](../src/raphael/backtracking.py)
[Backtracking graphe](backtracking_graphe.md)|Backtracking avec graphe implicite et arbre de décision|[backtracking_graphe.py](../src/raphael/backtracking_graphe.py)
[Force brute](brute_force.md)|Force brute|[brute_force.py](../src/matteo/brute_force.py)
[Échange](swap.md)|Échange basé sur l'aléatoire|[swap.py](../src/matteo/swap.py)
[Masque](mask.md)|Backtracking avec matrice d'entiers et tangage des numéros de colonne|[mask.py](../src/raphael/mask.py)
[Conflits min](min_conflicts.md)|Choix aléatoire de la case la moins menacée|[min_conflicts.py](../src/paolo/min_conflicts.py)
[Ping pong](pingpong.md)|Basé sur la force brute|[ping_pong.py](../src/marius/pingpong.py)
[Aléatoire](random.md)|Utilisation de l'aléatoire|[aleatoire.py](../src/matteo/random.py)
[Symétrie](symetrie.md)|Backtracking 2 par 2 reines|[symetrie.py](../src/marius/symetrie.py)

## Compléments

### 1. La fonction is_valid()

#### Explication

La fonction vérifie si la liste de résultat est correcte autrement dit, si la liste les reines sont biens placé

Le résultat est représenter de cette manière [2,0,3,1] ce qui représente les coordonnés de la ligne suivant la colonne en indice

ce qui donne :

    . Q . .
    . . . Q
    Q . . .
    . . Q .

Pour cela :

La fonction parcours la liste de résultat comme un algorithme de recherche et compare deux valeurs entre elles
Ainsi elle va regarder si les deux reines sélectionner sont sur la même ligne ou qu'elles sont sur la même diagonale

#### Vérification en colonne

    if tabResult[Reine1] == tabResult[Reine2]

Les reines sont obligatoirement sur des colonnes différentes car la colonne est représenter par l'indice de case. Ducoup, on vérifie si les reines sont sur la même ligne

#### Vérification des diagonales

    if |tabRes[i] - tabRes[j]| == |j - i|

Prenons l'exemple si dessous dans un cas avec deux reines sur un tableau d'ordre 4 :

    . . . .
    . . . Q
    Q . . .
    . . . .

Coordonnée de la reine 1 : (1,3)\
Coordonnée de la reine 2 : (2,0)\
Donc i vaut 0 et j vaut 3

$$\begin{split}
\lvert3 - 0\rvert &= \lvert1 - 2\rvert\\
\lvert3\rvert &= \lvert-1\rvert\\
3 &\neq 1
\end{split}$$

Les résultats sont différents donc les reines sont sur des diagonales différentes

## Idées d'optimisation supplémentaires

### 1 : backtracking en spirale

Résoudre la grille en faisant des des spirales vers l'extérieur dans le sens des aiguilles d'une montre.

D'abord trouvons une fonction pour obtenir les coordonnées de la prochaine case à partire de `tileNo`:

tileNo|0|1|2|3
-|-|-|-|-
**0**|0|1|2|3
**1**|4|5|6|7
**2**|8|9|10|11
**3**|12|13|14|15

tileNo|0|1|2|3|4
-|-|-|-|-|-
**0**|0|1|2|3|4
**1**|5|6|7|8|9
**2**|10|11|12|13|14
**3**|15|16|17|18|19
**4**|20|21|22|23|24

On voudrait 5, 6, 10, 9, 8, 4, 0, 1, 2, 3, 7, 11 ,15, 14, 13, 12

ou 1:1, 1:2, 2:2, 2:1, 2:0, 1:0, 0:0, 0:1, 0:2, 0:3, 1:3, 2:3, 3:3, 3:2, 3:1, 3:0

On pourrait partir de `n//2`:`n//2`, puis tanguer de plus en plus, verticalement et horizontalement? (comme dans l'algorithme du masque)
