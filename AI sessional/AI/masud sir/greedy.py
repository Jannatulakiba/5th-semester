import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = []
    
    # Push start node with its heuristic value
    heapq.heappush(priority_queue, (heuristic[start], start))
    
    while priority_queue:
        h, node = heapq.heappop(priority_queue)  # Get node with smallest heuristic
        if node in visited:
            continue
        
        print(node, end=" ")   # Visit node
        visited.add(node)
        
        if node == goal:
            print("\nGoal reached!")
            return
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (lower = better/closer to goal)
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 2,
    'F': 0   # Goal
}

print("Best First Search Traversal:")
best_first_search(graph, 'A', 'F', heuristic)
