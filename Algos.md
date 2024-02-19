# S2.02 Sujet 2 - Algorithmes

On a un échiquier de N\*N cases, déterminer les agencements possibles de N reines.

Une reine doit être unique dans sa ligne, sa colonne et sa diagonale

## Approches algorithmiques

## Le brute Force

Incrémente de 1 chaque indice du tableau de résultat
quand le premier élément arrive à la limite n.
On réalise un modulo de n et incrémente de 1 au secon élément

Le tableau de resultat est sous forme d'une liste d'ordre n
chaque valeur représente le numéro de ligne pour le numéro de colonne en indice

## Marius

On place les dames sur toutes les premières cases de l'échiquier

Dès qu'une dame est en conflit, on l'avance d'une case.

<https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_huit_dames>

## Graphe

### Backtracking

Comme pour le sudoku

## Critère de comparaisons

### Temps

### Mémoire
