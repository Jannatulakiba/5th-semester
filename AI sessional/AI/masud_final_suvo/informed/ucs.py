import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Define the graph
G = nx.Graph()
edges = [
    ('A', 'B', 1), ('A', 'C', 3),
    ('B', 'D', 1), ('B', 'E', 4),
    ('C', 'F', 2), ('C', 'G', 4),
    ('E', 'G', 1),
    ('F', 'H', 3)
]
G.add_weighted_edges_from(edges)

# Visualization
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

# Uniform Cost Search (correct version)
def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    best_cost = {start: 0}
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        
        # If we reached goal, done
        if node == goal:
            draw_graph(graph, path, f"UCS Path (Cost = {cost})")
            return path, cost
        
        # Expand neighbors
        for neighbor in graph.neighbors(node):
            new_cost = cost + graph[node][neighbor]['weight']
            
            # Only add if cheaper than known cost
            if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                best_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
    
    return None, float('inf')

# Run UCS
path, total_cost = ucs(G, 'A', 'G')
print(f"UCS Path: {path}, Total Cost: {total_cost}")
