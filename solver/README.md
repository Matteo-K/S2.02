# Solver des N reines

## Usage

`./main.py <N> <algorithme>`

option|description
-|-
`-b`, `--benchmark`|Mesurer la performance (temps & mémoire) de l'algorithme au lieu de résoudre
`-v`, `--verbose`|Afficher la sortie verbeuse
`-h`, `--help`|Afficher l'aide

### Examples

Résoudre en $N=4$ avec le *backtracking*

`./main.py 4 backtracking`

Mesurer la performance en $N=3$ avec le *brute_force*

`./main.py 3 brute_force -b`
