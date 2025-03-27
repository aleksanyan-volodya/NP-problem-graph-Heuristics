### K-coloriage

Nous avons suivi l'algorithme heuristique vu en cours de k-coloriage 
et nous avons décidé de l'implémenter en python .

#### Structure du graphe
La structure d'un graphe est représentée comme un dictionnaire avec en clefs les noeuds et en valeur la liste des noeuds liés
Un coloriage est ici représenté comme un dictionnaire associant à chaque noeud une couleur (un nombre entier ici)

#### Algorithme 

Dans l'algorithme, on colorie le noeud de plus haut degré, puis on colorie de la même couleur le + de  noeuds possibles n'y étant pas connectés 
Puis on choisit un nouveau noeud de plus haut degré possible non coloré, et on recommence .
Il faut donc garder en mémoire les noeuds déjà coloriés, avoir accès au noeud de plus haut degré et pouvoir vérifier les couleur de ses voisins.
Il faut de + pouvoir vérifier que tout les noeuds ont bien été attribué d'une couleur (si le nombre de couleurs utilisés ne dépasse pas le seuil donné),
et pouvoir énumérer les noeuds n'étant pas nos voisins .
C'est pourquoi nous avons crée les fonctions respectives max_degre,neighbours_colors,is_colored et get_not_connected . 
L'algorithme est implémenté dans la fonction naive_coloration.
