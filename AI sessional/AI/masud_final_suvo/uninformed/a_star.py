import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Define the graph
G = nx.Graph()
edges = [
    ('A', 'B', 1), ('A', 'C', 3),
    ('B', 'D', 1), ('B', 'E', 4),
    ('C', 'F', 2), ('C', 'G',2),('E', 'G', 1),
    ('F', 'H', 3)
]
G.add_weighted_edges_from(edges)

# Define a heuristic: map each node to an estimate of cost to 'G'
# Ensure these do not overestimate to keep A* optimal
heuristic = {
    'A': 7, 'B': 6, 'C': 20, 'D': 3, 'E': 2, 'F': 1, 'G': 0
}

# Visualization function
def draw_graph(G, path=None, title="Graph"):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges})
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def reconstruct_path(parent, start, goal):
    if goal not in parent and start != goal:
        return None
    path = [goal]
    cur = goal
    while cur != start:
        cur = parent[cur]
        path.append(cur)
    path.reverse()
    return path

# A* algorithm (graph-search style)
def a_star(graph, start, goal, h):
    parent = {start: None}
    g = {start: 0.0}
    closed = set()
    # (f, g, node) in the heap
    pq = [(h[start], 0.0, start)]

    while pq:
        f_u, g_u, u = heapq.heappop(pq)
        if u in closed:
            continue
        if u == goal:
            path = reconstruct_path(parent, start, goal)
            draw_graph(graph, path, "A* Path")
            return path
        closed.add(u)

        for v in graph.neighbors(u):
            w = graph[u][v]['weight']
            tentative = g_u + w
            if v in closed and tentative >= g.get(v, float('inf')):
                continue
            if tentative < g.get(v, float('inf')):
                g[v] = tentative
                parent[v] = u
                heapq.heappush(pq, (tentative + h[v], tentative, v))
    return None

# Run A*
print("A* Path:", a_star(G, 'A', 'G', heuristic))
