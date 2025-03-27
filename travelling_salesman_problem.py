import random

def random_graph_generator(n=10, m=0.5, min_w=1, max_w=20) -> dict:
    """
    n: number of nodes
    m: probability of edge creation
    min_w: minimum weight of an edge
    max_w: maximum weight of an edge

    return: a random graph in form of a dictionary of dictionaries
    
    ex :
    $ random_graph_generator(4, 0.5, 1, 10)
    
    > {1: {       2: 10,           },
    >  2: {1: 10,        3: 2, 4: 8},
    >  3: {       2: 2,        4: 6},
    >  4: {       2: 8, 3: 6       }}

    """
    G = {}
    for i in range(1,n+1):
        G[i] = {}
        for j in range(1, i):
            if random.random() < m:
                val = random.randint(min_w,max_w)
                G[i][j] = val
                G[j][i] = val
    return G

def path_weight(G, path) -> int:
    """
    G: a graph in form of a dictionary of dictionaries
    path: a list of nodes

    return: the weight of the path in the graph if exists, None otherwise
    
    ex:
    $ path_weight(graph, [1,2,3,4,5,6,7,1])
    
    > 69
    """
    try:
        weight = 0
        node = path[0]
        for i in range(1,len(path)):
            node_next = path[i]
            weight += G[node][node_next]
            node = node_next
        return weight
    except:
        return None
    

def best_path(G, path) -> tuple:
    """
    G: a graph in form of a dictionary of dictionaries
    path: a list of nodes

    return: a tuple of the best path and its weight

    ex:
    $ best_path(graph, [1,2,3,4,5,6,7,1])

    > ([1, 2, 4, 3, 5, 6, 7, 1], 65)
    """
    best = (path, path_weight(G, path))
    for i in range(1,len(path)-2):
        for j in range(i+1,len(path)-1):
            path_i_j = path.copy()

            path_i_j[i], path_i_j[j] = path_i_j[j], path_i_j[i]
            weight = path_weight(G, path_i_j)

            if (weight is not None) and weight < best[1]:
                best = (path_i_j, weight)

    return best


def loop_over_paths(G, path) -> tuple:
    """
    G: a graph in form of a dictionary of dictionaries
    path: a list of nodes

    return: the best path and its weight

    ex:
    $ loop_over_paths(graph, [1,2,3,4,5,6,7,1])

    > ([1, 2, 4, 6, 5, 3, 7, 1], 64)
    """
    best = best_path(G, path)
    weight = best[1]-1 # initial value

    while best[1] != weight:
        path, weight = best
        best = best_path(G, path)
    return best

if __name__ == "__main__":
    graph = {1:{      2:12, 3:10,                 7:12},
         2:{1:12,       3:8, 4:12                 },
         3:{1:10, 2:8,       4:11, 5:3,       7:9 },
         4:{      2:12, 3:11,      5:11, 6:10     },
         5:{            3:3, 4:11,       6:6, 7:7 },
         6:{                 4:10, 5:6,       7:9 },
         7:{1:12,       3:9,       5:7,  6:9      }
         }
    
    print(best_path(graph, [1,2,3,4,5,6,7,1]))
    #print(loop_over_paths(graph, [1,2,3,4,5,6,7,1]))