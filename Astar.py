import networkx as nwx
graph=nwx.Graph()
while True:
  choice=int(input("Want to insert nodes and edges? Press 1 for yes and 2 for no"))
  if choice==1:
    node1=input("enter node1").strip().upper()
    node2=input("enter node2").strip().upper()
    weight=int(input("Enter weight between node1 and node2"))
    graph.add_edge(node1,node2,weight=weight)
  else:
    break

graph.adj.items()
for node,neighbors in graph.adj.items():
  print(node,neighbors)

start=input("enter start node").strip().upper()
goal=input("enter goal node").strip().upper()
graph.nodes()

heuristic_value={}
heuristic_value[goal]=0
for node in graph.nodes():
  if node!=goal:
    heuristic_val=int(input(f"enter heuristic value from node{node} to goal{goal}"))
    heuristic_value[node]=heuristic_val
heuristic_value

def get_heuristic(u,v):
  return heuristic_value[u]
path=nwx.astar_path(graph,start,goal,heuristic=get_heuristic,weight='weight')
total_cost=nwx.astar_path_length(graph,start,goal,heuristic=get_heuristic,weight='weight')
print("Optimal path:","->".join(path))
print("total cost:",total_cost)

