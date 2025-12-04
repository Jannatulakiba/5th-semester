

def dfs(tree, start, visited=None):
    if visited is None:   # ✅ default mutable list এড়াতে
        visited = []
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
    for node in tree[start]:
        dfs(tree, node, visited)

# --- ইউজার থেকে ইনপুট নেওয়া ---
s = input("Enter graph (ex: A:B,C B:D,E C:F D: E: F:): ")
tree = {}
for p in s.split():
    node, neighbors = p.split(":")
    if neighbors:
        tree[node] = neighbors.split(",")
    else:
        tree[node] = []

start_node = input("Enter start node: ").strip()

print("DFS Traversal:")
dfs(tree, start_node)
