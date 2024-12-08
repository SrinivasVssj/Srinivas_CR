print("Try programiz.pro")
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")
stack = []
visited = set()
graph = {1:[2,3],2:[1,4],3:[1,4],4:[2,3]}
root = 1
stack.append(root)
while stack:
    node = stack.pop()
    if node not in visited:
        visited.add(node)
        print(str(node)+ f" visited and it's neighbours are {n}" for n in graph[node])
        stack.extend([neighbor for neighbor in graph[node] if neighbor not in visited])