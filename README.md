# Problème des N reines

## Solveur

`./solve.py <N> <algorithme>`

option|description
-|-
`-b [TIMES]`, `--benchmark [TIMES]`|Mesurer la performance (temps & mémoire) de l'algorithme au lieu de résoudre. L'argument donne le nombre d'exécutions (200 par défaut)
`-v`, `--verbose`|Afficher la sortie verbeuse
`-h`, `--help`|Afficher l'aide

### Examples

Résoudre en $N=4$ avec le *backtracking*

`./solve.py 4 backtracking`

Mesurer la performance en $N=3$ avec le *brute_force*

`./solve.py 3 brute_force -b`

Mesurer la performance en $N=3$ avec le *brute_force* avec 100 exécutions

`./solve.py 3 brute_force -b 100`

### Todo

- Marius' techniques
