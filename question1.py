def bfs_traversal(graph, initial_node) -> list:
    # your implementation here
    # your function will return a list!
    queue = [initial_node]              # initialize queue and visited set
    visited = []

    while queue:                        # while there are nodes left in the queue
        node = queue.pop(0)             # pop node from the left side (FIFO order)
        if node not in visited:
            visited.append(node)        # append the node if it hasn't already been visited
        for child in graph[node]:       # for each of the node's children
            if child not in visited:
                queue.append(child)     # append the child if it has not already been visited
    
    return visited

def main() -> None:
    graph = {"+": ["*",3], "*":[2,7], 2:[],7:[],3:[]}
    initial_node = "+"
    graph2 = {0: [1,3], 1:[2,3], 2:[3,1], 3:[0,1]}
    initial_node2 = 0
    print(f'Test 1: {bfs_traversal(graph, initial_node)}')
    print(f'Test 2: {bfs_traversal(graph2, initial_node2)}')

if __name__ == '__main__':
    main()