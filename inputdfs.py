def get_graph():
  no_of_nodes=int(input("Enter the no of nodes:"))
  graph={}
  for i in range(no_of_nodes):
    node=input(f"enter node{i+1}:")
    no_of_edge=int(input("no of edge this node has:"))
      
    edge=[]
    for j in range(no_of_edge):
      node_connected=input("enter connected node:")
      edge.append(node_connected)
    graph[node]=edge
  return graph

def dfs(st,goal,graph,vis=None):
  if vis is None:
    vis=set()
  print(st)
  if st==goal:
    return True
  vis.add(st)
  for child in graph[st]:
    if child not in vis:
      if dfs(child,goal,graph,vis):
        return True
  return False



graph=get_graph()
st=input("enter start:")
goal=input("enter the goal:")
dfs(st,goal,graph)
