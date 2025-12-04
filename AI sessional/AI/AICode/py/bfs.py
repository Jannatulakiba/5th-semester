from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

str = input("Graph: ")#A:B,C B:D,E C:F D: E: F:

graph = {}


for p in str.split():
    node, neighbors = p.split(":")
    if neighbors:
        graph[node] = neighbors.split(",")
    else:
        graph[node] = []

start_node = input("Where to start : ")#A

print("BFS traversal:")
bfs(graph, start_node)
