import networkx as nx
import matplotlib.pyplot as plt

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

# DFS Limited algorithm
def dfs_limited(graph, start, goal, depth_limit):
    def recursive_dfs(node, path, depth):
        if depth > depth_limit:
            return None
        if node == goal:
            return path
        for neighbor in graph.neighbors(node):
            if neighbor not in path:
                result = recursive_dfs(neighbor, path + [neighbor], depth + 1)
                if result:
                    return result
        return None
    
    path = recursive_dfs(start, [start], 0)
    if path:
        draw_graph(graph, path, f"DFS Limited (Depth {depth_limit}) Path")
    return path

# Run DFS Limited
print("DFS Limited Path:", dfs_limited(G, 'A', 'G', 4))