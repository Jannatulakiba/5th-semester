import networkx as nx
import matplotlib.pyplot as plt

# Define the tree graph (directed)
G = nx.DiGraph()
edges = [
    ('A', 'B', 1), ('A', 'C', 3),
    ('B', 'D', 1), ('B', 'E', 4),
    ('C', 'F', 2), ('C', 'G',2),('E', 'G', 1),
    ('F', 'H', 3)
]
G.add_weighted_edges_from(edges)

# Visualization function
def draw_graph(G, path=None, title="Tree Graph"):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges})
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2, arrows=True)
    plt.title(title)
    plt.show()

# Iterative DFS algorithm
def iterative_dfs(graph, start, goal):
    depth_limit = 0
    def recursive_dfs(node, path, depth):
        if depth > depth_limit:
            return None
        if node == goal:
            return path
        for neighbor in graph.successors(node):
            if neighbor not in path:
                result = recursive_dfs(neighbor, path + [neighbor], depth + 1)
                if result:
                    return result
        return None
    
    while True:
        result = recursive_dfs(start, [start], 0)
        if result:
            draw_graph(graph, result, "Iterative DFS Path")
            return result
        depth_limit += 1
        if depth_limit > len(graph.nodes):
            return None

# Run Iterative DFS
print("Iterative DFS Path:", iterative_dfs(G, 'A', 'G'))