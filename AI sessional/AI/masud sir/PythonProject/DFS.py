from collections import deque

def dfs(g, s):
    queue=deque([s])
    visited=set()

    while queue:
        vertex=queue.pop()
        if vertex not in visited:
            print(vertex,end=" ")
            visited.add(vertex)

            for n in g[vertex]:
                if n not in visited:
                    queue.append(n)

str = input("Graph: ")
graph={}

for p in str.split():
    node,neighbor= p.split(":")
    if neighbor:
        graph[node]= neighbor.split(",")
    else:
        graph[node]=[]

start=input("Enter start node: ")
dfs(graph,start)