def dfs(v):
    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs(i)

n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))
visited = [0 for _ in range(n)]

for i in range(n):
    dfs(i)
    print(*visited)
    visited = [0 for _ in range(n)]