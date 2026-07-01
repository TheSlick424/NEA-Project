def a_star_algorithm(node_dict, start, goal):
    THE_path = {}
    shortest_path = []

    for node in node_dict:
        THE_path[node] = {"Path Distance": float("inf"),
                          "Heuristic": 0,
                          "Combined Distance": float("inf"),
                          "Previous Node": None}

    THE_path[start]["Combined Distance"] = 0
    THE_path[start]["Path Distance"] = 0

    while node_dict:
        shortest = None

        for node in node_dict:
            if shortest is None:
                shortest = node
            elif THE_path[node]["Combined Distance"] < THE_path[shortest]["Combined Distance"]:
                shortest = node


        for neighbour, path_cost in node_dict[shortest].items():
            if neighbour in node_dict and THE_path[shortest]["Path Distance"] + node_dict[shortest][neighbour] < THE_path[neighbour]["Path Distance"]:
                THE_path[neighbour]["Path Distance"] = THE_path[shortest]["Path Distance"] + node_dict[shortest][neighbour]
                THE_path[neighbour]["Combined Distance"] = THE_path[neighbour]["Path Distance"] + THE_path[neighbour]["Heuristic"]
                THE_path[neighbour]["Previous Node"] = shortest

        node_dict.pop(shortest)

    current_node = goal
    while current_node is not start:
        shortest_path.insert(0, current_node)
        current_node = THE_path[current_node]["Previous Node"]

    shortest_path.insert(0, start)
    print(shortest_path)

node_dic = {"Node 1": {"Node 2": 4, "Node 3": 3, "Node 4": 2},
             "Node 2": {"Node 1": 4, "Node 5": 4},
             "Node 3": {"Node 1": 3, "Node 4": 5},
             "Node 4": {"Node 1": 2, "Node 3": 5, "Node 6": 2},
             "Node 5": {"Node 2": 4, "Node 7": 2},
             "Node 6": {"Node 4": 2, "Node 7": 10},
             "Node 7": {"Node 5": 2, "Node 6": 10}}
a_star_algorithm(node_dic, "Node 1", "Node 7")