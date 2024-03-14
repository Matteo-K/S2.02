# Backtracking graphe

Version de du [backtracking](../backtracking/backtracking.md) utilisant les graphes.

Se base sur le principe d'une machine à états finis

Transition : placement d'une nouvelle reine

On peut décrire cette stratégie par un graphe dont les sommets sont les différents états du jeu et les arêtes représentent les transitions d'un état à un autre. Dans le cas qui nous intéresse, le graphe ne possède pas de cycle (pas de retour possible), c'est donc un arbre appelé arbre de décision (<https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision>).

Le jeu commence donc avec un échiquier vide et on change d'état à chaque fois qu'une nouvelle reine est placée.

Il y a 8 façons possibles de placer la première reine sur la première colonne. Il s'agit ensuite de déterminer à quelle ligne placer la deuxième reine et ainsi de suite. On peut ainsi représenter une solution par un vecteur (de longueur 8) contenant les numéros de lignes où se trouvent nos huit reines.

Il s'agit d'un parcours dans un graphe implicite (<https://en.wikipedia.org/wiki/Implicit_graph>).

---

Cela signifie que les sommets du graphes sont des vecteurs de 8 lignes où placer chaque reine.

Les arrêtes représented l'ajout d'une reine à une ligne et une colonne.

Donc l'arbre a 9 niveaux en comptant le noeud racine, un vecteur vide.

L'objectif est de trouver toutes les solutions.

```mermaid
flowchart LR
    start[" "]
    start --> 0
    start --> 1
    start --> 2
    start --> 3
    start --> 4
    start --> 5
    start --> 6
    start --> 7
```

## Contraintes de validité des numéros de ligne

Entrée :

- `c` : numéro de colonne en cours de traitement
- `S` : le vecteur des lignes
- `g` : la matrice de booléens représentant la grille (vrai si libre)

$\forall l \in \N \cap [0;8[$ souhaitant être ajouté au vecteur solution $S$,

- Ligne libre : $l \notin S$
- Diagonale NE SO : $g_{i,\ j}$ pour tous $i,\ j$ de $d_{NE\_SO}(l, c)$ à $N$
- Diagonale SE NO : $g_{i,\ j}$ pour tous $i,\ j$ de $d_{SE\_NO}(l, c)$ à $0$

## scratch

comment itérer sur les cases formant la NE_SO?

$$d_{NE\_SO}(l, c) \to \begin{align*}
a &= l + c\\
d_l &= min(a, N)\\
d_c &= a - l_d\\
\end{align*}$$

parcours : $d_l+i$, $c_l+j$

pour SE_NO:

$$d_{SE\_NO}(l, c) \to \begin{align*}
a &= l - c\\
d_l &= N - max(0, a)\\
d_c &= N - max(0, -a)
\end{align*}$$

parcours : $d_l-i$, $c_l-j$

### diagonals 2

so this doesnt seem to work:

coords|ne_so|se_no
-|-|-
0,0|0,0|3,3
0,1|0,1|2,3
0,2|0,2|1,3
0,3|0,3|0,3
1,0||
1,1||
1,2||
1,3||
2,0||
2,1||
2,2||
2,3||
3,0||
3,1||
3,2||
3,3||

## possibleRows

we need to implement the backtracking properly, so we need a way to rewind in the solving process.

we proceed column by column and then row by row

On s'aperçoit que toutes les lignes comme toutes les colonnes seront présentes exactement une fois dans la solution.

disons que si il n'y a pas de ligne valide pour la colonne *c*,
ça veut dire que notre début solution est incorrect et qu'on arrive dans un sans-issue dans l'arbre de décision.

on doit donc faire marche arrière, cad repartir à la colonne précédente et prendre la ligne suivante.
