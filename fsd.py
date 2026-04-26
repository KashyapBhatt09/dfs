def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# User Input
graph = {}

n = int(input("Enter number of vertices: "))
for i in range(n):
    node = input("Enter vertex name: ")
    graph[node] = []

e = int(input("Enter number of edges: "))
for i in range(e):
    u, v = input("Enter edge (u v): ").split()
    graph[u].append(v)
    graph[v].append(u)

start = input("Enter starting vertex: ")

visited = set()

print("DFS Traversal:")
dfs(graph, start, visited)
