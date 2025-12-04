graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node , goal): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ")
    if (m == goal):          # jodi 5 thika 3 r path dekte chai sudu
      print ("\nGoal Node " + goal + " Found\n")
      return
    

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
    

# Driver Code
goal = input('Enter the goal node:-')
print("Following is the Breadth-First Search")
bfs(visited, graph, '5' , goal)    # function calling