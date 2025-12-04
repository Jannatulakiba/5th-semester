from collections import deque

def bidirectional_bfs(g, start, goal):
    if start == goal:
        print("Start and goal are the same:", start)
        return

    visited_start = {start}
    visited_goal = {goal}

    queue_start = deque([start])
    queue_goal = deque([goal])

    while queue_start and queue_goal:
        curr_start = queue_start.popleft()
        for neighbor in g.get(curr_start, []):
            if neighbor in visited_goal:
                print("Path found via:", neighbor)
                return
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                queue_start.append(neighbor)

        curr_goal = queue_goal.popleft()
        for neighbor in g.get(curr_goal, []):
            if neighbor in visited_start:
                print("Path found via:", neighbor)
                return
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                queue_goal.append(neighbor)

    print("No path found.")

s = input("Graph: ")  # Example: A:B,C B:D,E C:F D: E: F:
graph = {}

for p in s.split():
    node, neighbors = p.split(":")
    if neighbors:
        graph[node] = neighbors.split(",")
    else:
        graph[node] = []

start_node = input("Start node: ")
goal_node = input("Goal node: ")

bidirectional_bfs(graph, start_node, goal_node)