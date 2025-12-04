def dls(graph, node, limit, visited):
    if limit < 0:
        return
    print(node, end=" ")
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dls(graph, neighbor, limit - 1, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dls(graph, 'A', 3,[])