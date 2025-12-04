import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [start])]   # (cost, node, path)
    visited = set()
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return path, cost
        
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path + [neighbor]))
    return None


# Example weighted graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

print(ucs(graph, 'A', 'F'))
