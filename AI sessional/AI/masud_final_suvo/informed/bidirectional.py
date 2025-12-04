import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Define the tree graph (directed)
G = nx.DiGraph()
edges = [
    ('A', 'B', 1), ('A', 'C', 3),
    ('B', 'D', 1), ('B', 'E', 4),
    ('C', 'F', 2), ('C', 'G', 2), ('E', 'G', 1),
    ('F', 'H', 3)
]
G.add_weighted_edges_from(edges)

# Visualization function
def draw_graph(G, path=None, title="Tree Graph", explored_start=None, explored_goal=None):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    
    colors = []
    for node in G.nodes():
        if explored_start and node in explored_start:
            colors.append('skyblue')
        elif explored_goal and node in explored_goal:
            colors.append('lightgreen')
        else:
            colors.append('lightgray')
    
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800, font_size=12, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges})
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3, arrows=True)
    
    plt.title(title)
    plt.show()

# Correct Bidirectional Search
def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    queue_start = deque([(start, [start])])
    queue_goal = deque([(goal, [goal])])
    visited_start = {start: [start]}
    visited_goal = {goal: [goal]}

    while queue_start and queue_goal:
        # Expand from start side
        node_s, path_s = queue_start.popleft()
        for neighbor in graph.successors(node_s):
            if neighbor not in visited_start:
                visited_start[neighbor] = path_s + [neighbor]
                queue_start.append((neighbor, path_s + [neighbor]))
            if neighbor in visited_goal:
                path = visited_start[neighbor] + visited_goal[neighbor][::-1][1:]
                draw_graph(graph, path, "Bidirectional Search: Meet in the Middle",
                           explored_start=visited_start.keys(), explored_goal=visited_goal.keys())
                return path
        
        # Expand from goal side
        node_g, path_g = queue_goal.popleft()
        for neighbor in graph.predecessors(node_g):  # go backward from goal
            if neighbor not in visited_goal:
                visited_goal[neighbor] = path_g + [neighbor]
                queue_goal.append((neighbor, path_g + [neighbor]))
            if neighbor in visited_start:
                path = visited_start[neighbor] + visited_goal[neighbor][::-1][1:]
                draw_graph(graph, path, "Bidirectional Search: Meet in the Middle",
                           explored_start=visited_start.keys(), explored_goal=visited_goal.keys())
                return path

        # Optional visualization of exploration
        draw_graph(graph, explored_start=visited_start.keys(),
                   explored_goal=visited_goal.keys(),
                   title="Bidirectional Search Progress")

    return None

# Run Bidirectional Search
print("Bidirectional Search Path:", bidirectional_search(G, 'A', 'G'))
