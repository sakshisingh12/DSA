import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
graph = [ [] for _ in range(n+1) ]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]

visited = [ False for _ in range(n+1) ]

def DFS(v, visited, graph):
    
    visited[v] = True

    for adj in graph[v]:
        if not visited[adj]:
            DFS(adj, visited, graph)


src = []

for i in range(n):
    if not visited[i+1]:
        DFS(i+1, visited=visited, graph=graph)
        src += [i+1]


roads = len(src) - 1
print(roads)
for i in range(roads):
    print(src[i], src[i+1])

