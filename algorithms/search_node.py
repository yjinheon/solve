def search_shortest_route(connection_info, start_node, end_node, route=[]):
    route = route + [start_node]
    if start_node == end_node:
        return route
    if not connection_info.__contains__(start_node):
        return None
    
    shortest = None
    for node in connection_info[start_node]:
        
        if end_node in connection_info[start_node]:
            shortest = route + [end_node]
            return shortest
        
        if node not in route:
            res = search_shortest_route(connection_info,node,end_node,route)
            
            



if __name__ ==  "__main__":
    connection_info = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }
    print(search_shortest_route(connection_info, 'B', 'D'))
