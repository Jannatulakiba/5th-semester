import heapq
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 3), ('D', 1)],
    'B': [('D', 2)],
    'C': [('G', 5)],
    'D': [('G', 1)],
    'G': []
}
heuristic = {'S': 7, 'A': 6, 'B': 4, 'C': 5, 'D': 2, 'G': 0}
def a_star(start, goal):
    pq = [(heuristic[start], 0, start)]   # (f, g, h)
    visited = set()
    while pq:
        f, g, node = heapq.heappop(pq)
        if node in visited and visited[node] <= g:
            continue
        print("Visiting:", node)
        visited.add(g)
        if node == goal:
            print("Goal reached with cost:", g)
            return
        for neighbor, cost in graph.get(node,[]):          # <-- এখানে .items() না
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor))

a_star('S', 'G')
