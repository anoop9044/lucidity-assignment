def min_path(graph, initial, restaurants, customers):
    path = [initial]
    # print(graph.weights[(initial, restaurants[0])])
    next_node = min(restaurants, key=lambda k: graph.weights[(initial, k)])
    visited = {initial, next_node}
    current = next_node
    index_next_node = restaurants.index(next_node)
    restaurants.pop(index_next_node)
    to_deliver = [customers[index_next_node]]
    customers.pop(index_next_node)
    path = [initial, current]
    while restaurants or to_deliver:
        next_node = min(restaurants + to_deliver, key=lambda k: graph.weights[(current, k)])
        visited.add(next_node)
        path.append(next_node)
        if next_node in to_deliver:
            to_deliver.remove(next_node)
        else:
            index_next_node = restaurants.index(next_node)
            restaurants.pop(index_next_node)
            to_deliver.append(customers[index_next_node])
            customers.pop(index_next_node)
        current = next_node
    return path
