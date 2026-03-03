from collections import deque
graph={
  "A":["B","C"],
  "B":["D","F","E"],
  "C":["D","F"],
  "D":["E","F"],
  "E":["F"],
  "F":[]
}
def bfs(st,goal):
  vis=set()
  queue=deque([st])
  while queue:
    node=queue.popleft()
    print(node,end=" ")
    if(node==goal):
      print("\n Goal Found")
      return
    if node not in vis:
      vis.add(node)
      for neighbor in graph[node]:
        if neighbor not in vis:
          queue.append(neighbor)
bfs("A","F")
