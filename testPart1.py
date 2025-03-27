from part1 import *

exempl1 = {
    0: {2,3,5,9},
    1: {2,4,6,8},
    2: {0,1,3,4,5,6},
    3: {0,2,6},
    4: {1,2,5},
    5: {0,2,4},
    6: {1,2,3},
    8: {1},
    9: {0}
}

def is_n_colored(G,cols,n,partiellement=False):
    """
    Vérifie qu'une graphe est bien n-colorié (au + n couleurs utilisées) ,
    si partiellement=True, vérifie que le coloriage partiel est bien un n-coloriage , 
    sinon vérifie que tout les noeuds sont coloriés
    """
    nb_colors = len(set(([g for g in list(cols.values()) if g!=-1]))) # on calcule le nombre de couleurs distinctes (-1 correspond à un non-coloriage)
    if nb_colors > n:
        print('bruh')
        return False
    for noeud,conn in G.items():
        if partiellement:
            if (conn in neighbours_colors(G,cols,noeud)):
                return False
        else:
            if (conn in neighbours_colors(G,cols,noeud)) or conn==-1:
                return False
    return True

if __name__=="__main__":
    print("-------------------------------------------------")
    print("Exemple 1 :\n",exempl1," \nCe graphe est 4-coloriable " )
    color4_ex1 = naive_coloration(exempl1,4)
    color3_ex1=naive_coloration(exempl1,3)
    print("4-coloriage du premier exemple : ",color4_ex1)
    print(f"L'exemple 1 est 4 colorié :  {is_n_colored(exempl1,color4_ex1,4)} ")
        
    print("Et voici le 3-coloriage partiel du même graphe : ",naive_coloration(exempl1,3))
    print(f"L'exemple 1 est 3 colorié :  {is_n_colored(exempl1,color3_ex1,3)} ")
    print("-------------------------------------------------")