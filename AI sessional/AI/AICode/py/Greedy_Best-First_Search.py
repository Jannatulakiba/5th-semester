import heapq

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'G': []
}

heuristic = {'S': 7, 'A': 6, 'B': 4, 'C': 5, 'D': 2, 'G': 0}

def greedy_bfs(start, goal):
    pq = [(heuristic[start], start)]
    visited = set()

    while pq:
        h, node = heapq.heappop(pq)
        if node in visited: 
            continue
        print("Visiting:", node)
        visited.add(node)

        if node == goal:
            print("Goal reached!")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

greedy_bfs('S', 'G')
