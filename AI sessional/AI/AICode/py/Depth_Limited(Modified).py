def dfs_limited(tree, start, limit, visited=[]):
    if limit <= 0:
        return
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
    for node in tree[start]:
        dfs_limited(tree, node, limit-1, visited)

# --- গ্রাফ ইনপুট নেওয়া ---
s = input("Enter graph (ex: A:B,C B:D,E C:F D: E: F:): ")
tree = {}
for p in s.split():
    node, neighbors = p.split(":")
    if neighbors:
        tree[node] = neighbors.split(",")
    else:
        tree[node] = []

start_node = input("Enter start node: ").strip()
depth_limit = int(input("Enter depth limit: "))

print("DFS Limited Traversal:")
dfs_limited(tree, start_node, depth_limit)
