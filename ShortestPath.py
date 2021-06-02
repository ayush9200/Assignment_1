# With the help of both list and dictionary we are calculating shortest path from stating node to end node
# Below solution will work Questions B3 & B4

# Taking list with all edges and distance
edges = [['A', 'B', 5], ['B', 'C', 4], ['C', 'D', 8], ['D', 'C', 8], ['D', 'E', 6], ['A', 'D', 5], ['C', 'E', 2],
         ['E', 'B', 3],
         ['A', 'E', 7]]

# Taking dictionary with all edges and distances
edgesDict = {
    'A': [['B', 5], ['D', 5], ['E', 7]],
    'B': [['C', 4]],
    'C': [['D', 8], ['E', 2]],
    'D': [['C', 8], ['E', 6]],
    'E': [['B', 3]]
}

# We are considering Question (B3) -> The length of the shortest route (in terms of distance to travel) from A to C
# this assumes that there is a unique route
route = ['A', 'C']
startNode = route[0]
lastNode = route[len(route) - 1]
list_of_paths = []


# Method will print shortest path
def print_solution():
    print("--------------------- Shortest Path --------------------------------")
    print(f'Possible routes from {startNode} TO {lastNode}')
    min_dist = 0;
    count = 0
    index = 0
    for paths in list_of_paths:
        count + 1
        print(f' Path = {paths[0]} : Distance = {paths[1]}')
        if min_dist > paths[1] or min_dist == 0:
            min_dist = paths[1]
            index = count

    shortest = list_of_paths[index]
    print(f'Shortest path : {shortest[0]} with Distance : {min_dist}')


# Method will find most optimum solution for shortest route between two towns
def find_shortest_path():
    list_of_possible_routes = edgesDict[startNode]  #
    while_flag = True
    distance = 0
    path = ""
    while while_flag:
        for node in list_of_possible_routes:
            distance = 0
            path = startNode + " > "
            inner_list = []
            if lastNode is not node[0]:
                current_node = node[0]
                for edge in edges:
                    if edge[0] is current_node:
                        if edge[1] is lastNode:  # if immediate node is destination
                            distance = distance + int(node[1])
                            distance = distance + edge[2]
                            path = path + node[0] + " > " + edge[1]
                            inner_list.insert(0, path)
                            inner_list.insert(1, distance)
                            list_of_paths.append(inner_list)
                            break
                        else:               # if traversing further till we find destination
                            temp_last_node = edge[1]
                            for innerEdge in edges:
                                if innerEdge[0] is temp_last_node:
                                    if innerEdge[1] is lastNode:
                                        distance = distance + int(node[1])
                                        distance = distance + innerEdge[2] + edge[2]
                                        path = path + node[0] + " > " + temp_last_node + " > " + innerEdge[1]
                                        inner_list.insert(0, path)
                                        inner_list.insert(1, distance)
                                        list_of_paths.append(inner_list)
                                        break

                while_flag = False
            else:
                # print("Destination : ")
                while_flag = False
    print_solution()   # Calling method with all paths included in list
