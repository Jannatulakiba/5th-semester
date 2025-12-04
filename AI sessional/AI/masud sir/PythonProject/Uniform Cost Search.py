import heapq
def uniform_cost_search(g, start, goal):
    visited = set()
    queue = [(0, start, [])]  # (cost, node, path)

    while queue:
        cost, node, p = heapq.heappop(queue)
        if node in visited:
            continue
        p = p + [node]
        visited.add(node)
        if node == goal:
            return p, cost
        for neighbor, weight in g.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, p))
    return None, float('inf')

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

start_node = input("Where to start: ")
goal_node = input("Where to be end: ")

path, total_cost = uniform_cost_search(graph, start_node, goal_node)

print("Path:", path)
print("Total cost:", total_cost)