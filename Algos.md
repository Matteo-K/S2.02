# S2.02 Sujet 2 - Algorithmes

On a un échiquier de N\*N cases, déterminer les agencements possibles de N reines.

Une reine doit être unique dans sa ligne, sa colonne et sa diagonale

## Approches algorithmiques

### La fonction is_valid()

#### Expliquation

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

#### Vérification en colonne :

    if tabResult[Reine1] == tabResult[Reine2]

Les reines sont obligatoirement sur des colonnes différentes car la colonne est représenter par l'indice de case. Ducoup, on vérifie si les reines sont sur la même ligne

#### Vérification des diagonales :

    if |tabRes[i] - tabRes[j]| == |j - i|

Prenons l'exemple si dessous dans un cas avec deux reines sur un tableau d'ordre 4 :

    . . . .
    . . . Q
    Q . . .
    . . . .

Coordonnée de la reine 1 : (1,3)
Coordonnée de la reine 2 : (2,0)
Donc i vaut 0 et j vaut 3

    |3 - 0| == |1 - 2|
    |3| == |-1|
    3 != 1

Les résultats sont différentes donc les reines sont sur des diagonales différentes

### Le brute Force

Incrémente de 1 chaque indice du tableau de résultat

Quand le premier élément arrive à la limite n.
On réalise un modulo de n et incrémente de 1 au second élément et ainsi de suite

### Résolution par aléatoire

Choisi aléatoirement le numéro de ligne du placement pour chaque colonne.

la valeur est choisi entre 0 et n. Et ne peut pas être représenter deux fois dans la liste.

Les valeur sont initailisé avec range(0,n). Puis elles sont retirer de la liste range à chaque dès qu'elles sont sortit aléatoirement
La fonction essaye de résoudre le problème tant qu'elle n'a pas trouver de résolution correcte

Les temps varis beaucoup entre chaque taille différentes
Plus la grille est grande, plus le temps de recherche est long.

### échange

créer un tableau de résultat de 1 à n. 

vérifie si le tableau est correcte

sinon, on inverse un indice aléatoire avec son indice supérieur

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
|    12     | 0.015625  | 2.000000  |         0.616875         | 

Technique incrémentation :

| nb reines | temps min | temps max | temps moyen (exec 100 X) |
| :-------: | :-------: | :-------: | :----------------------: |
|     4     | 0.000000  | 0.015625  |      0.000313            |
|     5     | 0.000000  | 0.031250  |      0.000469            |
|     6     | 0.000000  | 0.078125  |      0.032344            |
|     7     | 0.046875  | 0.187500  |      0.128438            |
|     8     | 2.640625  | 5.500000  |      4.425000            |

|nb reines|    temps min    |    temps max    |  temps moyen    |
|:--------|:----------------|:----------------|:----------------|
|     4   |      0.000000   |      0.000000   |      0.000000   |
|     5   |      0.000000   |      0.000000   |      0.000000   |
|     6   |      0.000000   |      0.015625   |      0.000469   |
|     7   |      0.000000   |      0.015625   |      0.000156   | 
|     8   |      0.000000   |      0.015625   |      0.001250   | 
|     9   |      0.000000   |      0.031250   |      0.003438   |
|     10  |      0.000000   |      0.109375   |      0.013594   |
|     11  |      0.000000   |      0.187500   |      0.020469   |
|     12  |      0.000000   |      0.500000   |      0.089375   |

### Mémoire

#### a vérifier

 nb Reine | Backtracking | aléatoire | Incrémentation |
 :------: | :----------: | :-------: | :------------: |
     4    |     ...      |   62.96   |      0.24      |
     5    |     ...      |   26.56   |      0.24      |
     6    |     ...      |   29.12   |      0.00      |
     7    |     ...      |   31.36   |      0.00      |
     8    |     ...      |   33.04   |      0.00      |
     9    |     ...      |   25.76   |  |
    10    |     ...      |   27.44   |  |
    11    |     ...      |   32.48   |  |
    12    |     ...      |           |     28.56      |

