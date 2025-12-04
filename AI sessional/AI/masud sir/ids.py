def dls(graph, node, limit, visited):
    if limit < 0:
        return
    print(node, end=" ")
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dls(graph, neighbor, limit - 1, visited)

def ids(graph, start, max_limit):
    for i in range(max_limit):
        print(f"Iteration {i+1}: ", end="")
        dls(graph, start, i, [])
        print()

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

ids(graph, 'A', 4)
