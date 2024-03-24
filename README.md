# Problème des N reines

## Solveur - Exemples d'utilisation

Afficher l'aide

`./solve.py -h`\
`./solve.py --help`

Résoudre en $N=4$ avec le *backtracking*

`./solve.py 4 backtracking`

Mesurer la performance en $N=3$ avec le *brute_force*

`./solve.py 3 brute_force -b`

Mesurer la performance en $N=3$ avec le *brute_force* avec 100 exécutions

`./solve.py 3 brute_force -b 100`

## Création de graphiques - Exemples d'utilisation

Afficher l'aide

`./graph.py -h`\
`./graph.py --help`

Créer un graphique de l'utilisation mémoire moyenne avec $N\in[4;8]$, avec 100 exécutions, pour les algorithms *mask* et *backtracking_graphe*

`./graph.py mem 4 8 -b 100 mask backtracking_graphe`

Créer un graphique du temps CPU moyen avec $N\in[4;9]$, pour l'algorithme *backtracking_graphe*

`./graph.py time 4 9 mask backtracking_graphe`

Créer un graphique du temps CPU moyen avec $N\in[4;8]$, avec 50 exécutions, pour tous les algorithmes dont le nom commence par "backtracking"

`./graph.py time 4 8 -b 50 mask backtracking.*`

Créer un graphique du temps CPU moyen avec $N\in[6;7]$, pour tous l'algorithme *mask*

`./graph.py time 6 7 mask -Veia`

Créer un graphique du temps CPU médian avec $N\in[6;8]$, pour tous l'algorithme *mask*

`./graph.py time 6 8 mask -vEia`

Créer un graphique des temps CPU minimum et maximum avec $N\in[6;8]$, pour tous l'algorithme *mask*

`./graph.py time 6 9 mask -veIA`

### Todo

- Marius' techniques
- autocompute execution count so expected time is less than X ms
- add a way to list algorithms
