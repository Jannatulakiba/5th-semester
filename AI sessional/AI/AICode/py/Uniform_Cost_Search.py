import heapq
def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]  # (cost, node, path)
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)
        if node == goal:
            return path, cost
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    return None, float('inf')
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}


start_node = 'A'
goal_node = 'E'

path, total_cost = uniform_cost_search(graph, start_node, goal_node)

print("Path:", path)
print("Total cost:", total_cost)
