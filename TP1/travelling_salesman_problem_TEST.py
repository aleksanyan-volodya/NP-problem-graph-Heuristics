# travelling salesman problem test

import random
import travelling_salesman_problem as tsp
import Heuristcs as heu

def random_graph_generator(n=10, m=0.7, min_w=1, max_w=20) -> dict:
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

def find_hamiltonian_cycle(graph):
    """
    graph: a graph in form of a dictionary of dictionaries
    
    return: a list of nodes representing a Hamiltonian cycle
    """
    n = len(graph)
    path = []
    
    def backtrack(node, visited):
        if len(path) == n:
            if path[0] in graph[node]:
                path.append(path[0])
                return True
            return False
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                path.append(neighbor)
                visited.add(neighbor)
                if backtrack(neighbor, visited):
                    return True
                path.pop()
                visited.remove(neighbor)
        
        return False
    
    for start in graph:
        path = [start]
        if backtrack(start, {start}):
            return path
    
    return None  # No Hamiltonian cycle found

def print_graph(graph):
    for node in graph:
        print(node, ":", graph[node])

def test():
    graph = {1:{      2:12, 3:10,                 7:12},
         2:{1:12,       3:8, 4:12                 },
         3:{1:10, 2:8,       4:11, 5:3,       7:9 },
         4:{      2:12, 3:11,      5:11, 6:10     },
         5:{            3:3, 4:11,       6:6, 7:7 },
         6:{                 4:10, 5:6,       7:9 },
         7:{1:12,       3:9,       5:7,  6:9      }
         }
    
    print(([1, 2, 4, 3, 5, 6, 7, 1], 65) == tsp.best_path(graph, [1,2,3,4,5,6,7,1]))
    print(([1, 2, 4, 6, 5, 3, 7, 1], 64) == tsp.loop_over_paths(graph, [1,2,3,4,5,6,7,1]))

    graph = {1 : {2: 1, 4: 7, 5: 13, 6: 17},
             2 : {1: 1, 4: 10, 5: 4, 6: 16},
             3 : {4: 4, 5: 9, 6: 15},
             4 : {1: 7, 2: 10, 3: 4, 5: 1, 6: 4},
             5 : {1: 13, 2: 4, 3: 9, 4: 1},
             6 : {1: 17, 2: 16, 3: 15, 4: 4}
             }
    
    path = [1, 2, 4, 5, 3, 6, 1]
    print(([1, 2, 5, 4, 3, 6, 1], 42) == tsp.best_path(graph, path))
    print(([1, 2, 5, 3, 4, 6, 1], 39) == tsp.loop_over_paths(graph, path))


    graph = random_graph_generator(15, 0.7, 1, 20)
    path = find_hamiltonian_cycle(graph)
    print_graph(graph)
    print(f"{path = }")
    if path is not None:
        print("1 step: ", tsp.best_path(graph, path))
        print("normal: ", tsp.loop_over_paths(graph, path))
        print("2-OPT: ", heu.two_opt(graph, path))

if __name__ == "__main__":
    test()