import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Define the graph
G = nx.Graph()
edges = [
    ('A', 'B', 1), ('A', 'C', 3),
    ('B', 'D', 1), ('B', 'E', 4),
    ('C', 'F', 2), ('C', 'G', 2), ('E', 'G', 1),
    ('F', 'H', 3)
]
G.add_weighted_edges_from(edges)

# Heuristic (estimated distance to G)
heuristic = {
    'A': 7, 'B': 6, 'C': 20, 'D': 4,
    'E': 3, 'F': 2, 'G': 0, 'H': 3
}

# Visualization function
def draw_graph(G, path=None, title="Graph"):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=600, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges})
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
    plt.title(title)
    plt.show()

# Greedy Best-First Search algorithm
def greedy_best_first(graph, start, goal, heuristic):
    pq = [(heuristic[start], start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)
        if node == goal:
            draw_graph(graph, path, f"Greedy Best-First Path (Cost ≈ Heuristic {heuristic[node]})")
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))
    return None

# Run Greedy Best-First
print("Greedy Best-First Path:", greedy_best_first(G, 'A', 'G', heuristic))
