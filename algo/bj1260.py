import sys
def DFS(graph, start):
    visited = []
    stack = [start]
    i = 0
    while stack:
        i+=1
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n not in graph:
                return visited
            graph[n].sort(reverse=True)
            stack += graph[n]
    return visited

def BFS(graph, start):
    visited = []
    queue = [start]
    i = 0
    while queue:
        i+=1
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n not in graph:
                return visited

            graph[n].sort()
            queue += graph[n]
    return visited

N,M,V = map(int, sys.stdin.readline().split())
path = dict()

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    try:
        path[n1].append(n2)
    except:
        path[n1] = [n2]
    try:
        path[n2].append(n1)
    except:
        path[n2] = [n1]

for i in DFS(path,V):
    sys.stdout.write(str(i))
    sys.stdout.write(" ")
sys.stdout.write("\n")
for i in BFS(path,V):
    sys.stdout.write(str(i))
    sys.stdout.write(" ")
sys.stdout.write("\n")
