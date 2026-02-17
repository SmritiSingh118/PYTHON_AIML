def get_graph():
    no_of_nodes = int(input("Enter the no of nodes: "))
    graph = {}

    for i in range(no_of_nodes):
        node = input(f"Enter node {i+1}: ")
        no_of_edges = int(input("No of edges this node has: "))

        edges = []
        for j in range(no_of_edges):
            node_connected = input("Enter connected node: ")
            edges.append(node_connected)

        graph[node] = edges

    return graph   


def dfs(st, goal, graph, vis=None):
    if vis is None:
        vis = set()

    print(st)

    if st == goal:
        return True

    vis.add(st)

    for child in graph.get(st, []):
        if child not in vis:
            if dfs(child, goal, graph, vis):
                return True

    return False   


graph = get_graph()
st = input("Enter start: ")
goal = input("Enter the goal: ")

if dfs(st, goal, graph):
    print("Goal found!")
else:
    print("Goal not found!")
