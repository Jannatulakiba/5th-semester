import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Define the graph
G = nx.Graph()
edges = [
    ('A', 'B', 1), ('A', 'C', 3),
    ('B', 'D', 1), ('B', 'E', 4),
    ('C', 'F', 2), ('C', 'G',2),('E', 'G', 1),
    ('F', 'H', 3)
]
G.add_weighted_edges_from(edges)

# Visualization function
def draw_graph(G, path=None, title="Graph"):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges})
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.title(title)
    plt.show()

# BFS algorithm
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        if node == goal:
            draw_graph(graph, path, "BFS Path")
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

# Run BFS
print("BFS Path:", bfs(G, 'A', 'G'))