from collections import deque

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited[i] and graph[v][i]:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = 1
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(1, n+1):
            if not visited2[i] and graph[x][i]:
                q.append(i)
                visited2[i] = 1

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
visited2 = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(v)
print()
bfs(v)