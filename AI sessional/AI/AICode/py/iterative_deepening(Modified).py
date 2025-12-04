def dfs_limited(tree, start, limit, visited=None):
    if visited is None:
        visited = []
    if limit <= 0:
        return
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
    for node in tree.get(start, []):
        dfs_limited(tree, node, limit-1, visited)

def iterative_deepening(tree, start, max_limit):
    for i in range(max_limit):
        print(f"Iteration {i+1} : ", end="")
        dfs_limited(tree, start, i+1, [])
        print()

# --- ইউজার ইনপুট নেওয়া ---
s = input("Enter graph (ex: A:B,C B:D,E C:F D: E: F:): ")
tree = {}
for p in s.split():
    node, neighbors = p.split(":")
    if neighbors:
        tree[node] = neighbors.split(",")
    else:
        tree[node] = []

start_node = input("Enter start node: ").strip()
max_depth = int(input("Enter maximum depth limit: "))

print("\nIterative Deepening DFS Traversal:")
iterative_deepening(tree, start_node, max_depth)
