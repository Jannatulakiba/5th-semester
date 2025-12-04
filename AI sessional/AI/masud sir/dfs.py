def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    print(start, end=" ")     # Visit the node
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal:")
dfs(graph, 'A')
