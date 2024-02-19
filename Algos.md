# S2.02 Sujet 2 - Algorithmes

On a un échiquier de N\*N cases, déterminer les agencements possibles de N reines.

Une reine doit être unique dans sa ligne, sa colonne et sa diagonale

## Approches algorithmiques

### Le brute Force

Incrémente de 1 chaque indice du tableau de résultat
quand le premier élément arrive à la limite n.
On réalise un modulo de n et incrémente de 1 au secon élément

Le tableau de resultat est sous forme d'une liste d'ordre n
chaque valeur représente le numéro de ligne pour le numéro de colonne en indice

### Résolution par aléatoire

Choisi aléatoirement le numéro de ligne du placement pour chaque colonne
la valeur est choisi entre 0 et n. Et ne peut pas être représenter deux fois dans la liste.
les valeur sont initailisé avec range(0,n)
Puis les valeurs sont retirer de la liste range à chaque dès qu'elles sont sortit aléatoirement
La fonction essaye de résoudre le problème tant qu'elle n'a pas trouver de résolution correcte

Les temps varis beaucoup entre chaque taille différentes
Plus la grille est grande, plus le temps de recherche est long.

## Marius

On place les dames sur toutes les premières cases de l'échiquier

Dès qu'une dame est en conflit, on l'avance d'une case.

<https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_huit_dames>

## Graphe

### Backtracking

Comme pour le sudoku

## Critère de comparaisons

### Temps (en secondes)

Technique aléatoire :

| nb reines | temps min | temps max | temps moyen (exec 200 X) |
| :-------: | :-------: | :-------: | :----------------------: |
|     4     | 0.000000  | 0.015625  |         0.000078         |
|     5     | 0.000000  | 0.015625  |         0.000078         |
|     6     | 0.000000  | 0.031250  |         0.001172         |
|     7     | 0.000000  | 0.031250  |         0.000937         |
|     8     | 0.000000  | 0.031250  |         0.002812         |
|     9     | 0.000000  | 0.046875  |         0.008203         |
|    10     | 0.000000  | 0.250000  |         0.042500         |
|    11     | 0.000000  | 1.218750  |         0.152891         |

### Mémoire
