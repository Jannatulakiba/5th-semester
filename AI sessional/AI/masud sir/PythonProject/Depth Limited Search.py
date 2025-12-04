def depth_limited_search(g, start, goal, limit):
    def dfs(node, path, depth):
        if depth > limit:
            return None
        path = path + [node]
        if node == goal:
            return path

        for neighbor in g.get(node, []):
            r = dfs(neighbor, path, depth + 1)
            if r:
                return r
        return None

    return dfs(start, [], 0)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start_node = input("Where to start: ")
goal_node = input("Where to be end: ")
depth_limit = int(input("Depth limit: "))
result = depth_limited_search(graph, start_node, goal_node, depth_limit)
if result:
    print("Path found:", result)
else:
    print("No path found within depth limit.")