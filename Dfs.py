def dfs(start,goal,graph,vis=None,path=None):
    if vis is None:
        vis=set()
    if path is None:
        path=[]
    path.append(start)
    vis.add(start)
    print(start)
    if start==goal:
        return path
    for child in graph[start]:
        if child not in vis:
            if dfs(child,goal,graph,vis):
                return True
    return False 

graph1={'A':['B','C'],'B':['A','D','C','F'],'C':['A','F','D'],'D':['C','E','F','B'],
       'E':['F','D','B'],'F':['B','D','E','C']}
dfs('A','F',graph1)
