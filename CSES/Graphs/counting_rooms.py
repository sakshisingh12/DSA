import sys
sys.setrecursionlimit(10**7)

def get_num(graph, n, m):

    visited = [ [False for _ in range(m)] 
    for _ in range(n)]
    rooms = 0

    r, c = [ -1, 1, 0, 0 ], [ 0, 0, -1, 1 ]

    def dfs(i, j):

        visited[i][j] = True

        for k in range(4):
            dx, dy = i + r[k], j + c[k]

            if (dx >= 0) and (dx < n) and (dy >= 0) and (dy < m) and (not visited[dx][dy]) and (graph[dx][dy] == '.'):
                dfs(dx, dy)


    for i in range(n):
        for j in range(m):
            if (graph[i][j] == '.') and (not visited[i][j]):
                dfs(i, j)
                rooms += 1

    return rooms



def Solution():
    n, m = map(int, input().split(" "))
    graph = []

    for _ in range(n):
        row = input()
        graph.append(row)

    rooms = get_num(graph, n, m)
    print(rooms)


Solution()