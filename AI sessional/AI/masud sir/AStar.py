import heapq

def a_star_search(graph, start, goal, heuristic):
    # Priority queue: (f = g + h, node, path, g)
    pq = [(heuristic[start], start, [start], 0)]
    visited = set()
    
    while pq:
        f, node, path, g = heapq.heappop(pq)
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            print("Path found:", path)
            print("Total cost:", g)
            return
        
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(pq, (f_new, neighbor, path + [neighbor], g_new))

# Example weighted graph (Adjacency List with costs)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values (estimated cost to reach goal 'F')
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 7,
    'E': 1,
    'F': 0
}

print("A* Search:")
a_star_search(graph, 'A', 'F', heuristic)
