import travelling_salesman_problem as tsp

def two_opt(G, path):
    """
    2-OPT algorithm 
    """
    improved = True
    weight = tsp.path_weight(G, path)

    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path) - 1):
                new_path = path[:i] + path[i:j + 1][::-1] + path[j + 1:]
                new_weight = tsp.path_weight(G, new_path)

                if new_weight!=None and new_weight < weight:
                    path = new_path
                    weight = new_weight
                    improved = True

    return path, tsp.path_weight(G, path)

if __name__ == "__main__":
    graph = {1:{      2:12, 3:10,                 7:12},
         2:{1:12,       3:8, 4:12                 },
         3:{1:10, 2:8,       4:11, 5:3,       7:9 },
         4:{      2:12, 3:11,      5:11, 6:10     },
         5:{            3:3, 4:11,       6:6, 7:7 },
         6:{                 4:10, 5:6,       7:9 },
         7:{1:12,       3:9,       5:7,  6:9      }
         }
    
    print(tsp.best_path(graph, [1,2,3,4,5,6,7,1]))
    print(tsp.loop_over_paths(graph, [1,2,3,4,5,6,7,1]))
    print(two_opt(graph, [1,2,3,4,5,6,7,1]))