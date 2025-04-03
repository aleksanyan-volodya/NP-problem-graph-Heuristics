#################
# ALEKSANYAN Volodya
# COURNIL-RABEUX Clément
# LDD 3 IM
#################
import time

def schedul_greed(graph):
    """"
    Algo glouton pour l'allocation de registres
    @param graph: Dictionnaire représentant le graphe
    @return: Un dictionnaire associant chaque registre à une liste de variables
             et un dictionnaire associant chaque variable à son registre
    """
    couleurs = {}  # {variable: registre}
    
    for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):  # Trier par ordre décroissant de degré
        # Prendre les couleurs des voisins
        couleurs_voisins = {couleurs[neighbor] for neighbor in graph[node] if neighbor in couleurs}
        
        couleur = 0
        while couleur in couleurs_voisins:
            couleur += 1

        # Assigner cette couleur à la variable
        couleurs[node] = couleur
    
    # Construire le dict associée au probleme
    registers = {}
    for var, reg in couleurs.items():
        if reg not in registers:
            registers[reg] = []
        registers[reg].append(var)

    return registers, couleurs



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
    registers, couleurs = schedul_greed(graph)
    end_time = time.time()
    print("Temps d'exécution :", end_time - start_time)
    print("Nombre minimal de registres nécessaires :", len(registers))
    print("Affectation des registres :", registers)
    print("Mapping des variables :", couleurs)