import heapq
def ucs(graph,start,goal):
    pq= [(0,start,[start])]
    visited =set()

    while pq:
        cost,node,path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path,cost
        for neighbour, edge_cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq,(cost+edge_cost,neighbour,path+[neighbour]))
    return None            


graph={
    'A':[( 'B',1),( 'C',4)],
    'B':[( 'D',2),( 'E',5)],
    'C':[( 'F',1)],
    'D':[],
    'E':[( 'F',2)],
    'F':[]
}
print(ucs(graph,'A','F'))       