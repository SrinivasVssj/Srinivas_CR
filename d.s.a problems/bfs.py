# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")
from collections import deque
q = deque()
visited = set()
graph = {1:[2,3],2:[1,4],3:[1,4],4:[2,3]}
root = 1
q.append(root)
while q:
    print(q,visited)
    node = q.popleft()
    if node not in visited:
        visited.add(node)
        print(str(node)+ " visited and it's neighbours are",graph[node])
        q.extend([neighbor for neighbor in graph[node] if neighbor not in visited])
        print(q,visited)

    