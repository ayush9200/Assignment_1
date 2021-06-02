# With the help of list we are calculating distance of route stating first node to end node
# Below solution will work Questions A1, A2, A3 & A4

# Taking list with all edges and distance
edges = [['A','B',5],['B','C',4],['C','D',8],['D','C',8],['D','E',6],['A','D',5],['C','E',2],['E','B',3],
         ['A','E',7]]


# We are considering Question (A3) -> The distance of the route A-D-C
# this assumes that there is a unique route
def calculate_distance():
    route = ['A', 'D', 'C']
    distance = 0
    route_step = 0
    from_node = route[route_step]
    to_node = route[route_step+1]
    flag = True
    while flag:
        for edge in edges:
            if edge[0] is from_node:
                if edge[1] is to_node:  # If next node matched we will increment our distance and node covered
                    distance += edge[2]
                    route_step += 1
                    from_node = route[route_step]
                    if route_step+1 < len(route):
                        to_node = route[route_step+1]
                    if from_node is route[len(route)-1]:
                        flag = False

    # Printing result for above solution
    print("--------------------- Distance --------------------------------")
    print("Traversing through Route : "+str(route))
    print("Total Distance covered : "+str(distance))
    print("Total Nodes covered : " + str(route_step+1))
