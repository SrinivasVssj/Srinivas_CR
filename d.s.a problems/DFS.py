def dfs(node,graph,visited):
    if node in visited:
        return
    visited.add(node)
    print(str(node)+" visited")
    for neighbour in graph[node]:
        dfs(neighbour,graph,visited)
graph = {17:[19,20], 19:[17,30], 20:[17,30], 30:[19,20,35,40],35:[30],40:[35]}
root = 17
visited = set()
dfs(root,graph,visited)