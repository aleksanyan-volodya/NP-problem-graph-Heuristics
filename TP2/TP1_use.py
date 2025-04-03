#################
# ALEKSANYAN Volodya
# COURNIL-RABEUX Clément
# LDD 3 IM
#################

def max_degre(G,not_pic=[])->int:
    """
    return le sommet avec le plus haut degré, n'étant pas dans not_pic
    """
    m=-1
    m_s = None
    for k,s in G.items():
        if len(s)>m and not(k in not_pic):
            m=len(s)
            m_s = k
    return m_s


def neighbours_colors(G,cols,sommet):
    """
    @param1 G : dictionnaire associant à chaque noeud les noeuds auxquels il est connecté
    @param2 cols : dictionnaire associant à chaque noeud sa couleur (-1 : pas de couleur)
    @param3 sommet : le sommet courant qu'on regarde

    @return : donne toutes les couleurs des voisins du sommet 
    """
    return set([cols[neighbour] for neighbour in G[sommet]])

def is_colored(cols)->bool:
    """
    Vérifie si tout les noeuds sont bien coloriés
    """
    for s,col in cols.items():
        if col==-1:
            return False
    return True

def get_not_connected(G,sommet):
    """
    @param1 G : dictionnaire associant à chaque noeud les noeuds auxquels il est connecté
    @param2 sommet : le sommet courant qu'on regarde
    @return tout les sommets du graphe G n'étant pas connectés au sommet donné
    """
    return [s for s in list(G.keys()) if not(s in G[sommet])]

def schedul_greed(G):
    """
    @return : renvoie une coloration selon l'algorithme vu en cours avec max k couleurs
    """
    sommets = {sommet:-1 for sommet in list(G.keys())} # Hashmap des couleurs
    max_sommet = max_degre(G)
    color = 0
    dont_pick = [] # la liste des noeuds déjà coloriés
    while not(is_colored(sommets)): 
        sommets[max_sommet]=color
        dont_pick.append(max_sommet)
        for s in get_not_connected(G,max_sommet): # on boucle sur tout les sommets n'étant pas voisins
            if sommets[s]==-1 and not(color in neighbours_colors(G,sommets,s)): 
                # on colorie de la couleur courante seulement si le sommet n'est pas colorié 
                #ET que ses voisins n'ont pas cette même couleur
                sommets[s]=color
                dont_pick.append(s)
        max_sommet = max_degre(G,not_pic=dont_pick)
        color+=1

    return sommets

import time

if __name__ == "__main__":

    graph = {
        'a': {'b', 'c'},
        'b': {'a', 'c', 'd'},
        'c': {'a', 'b', 'd'},
        'd': {'b', 'c'},
        'e': {'c', 'f', 'g'},
        'f': {'e', 'g'},
        'g': {'e', 'f'}
    }
    start_time = time.time()
    registers = schedul_greed(graph)
    end_time = time.time()
    print("Temps d'exécution :", end_time - start_time)
    maxi = max(registers.values())+1
    print("Nombre minimal de registres nécessaires :", maxi)
    print("Affectation des registres :", registers)
