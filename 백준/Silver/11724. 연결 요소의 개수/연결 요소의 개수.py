def dfs(v):
    visit[v] = 1
    for i in graph[v]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [0] * (N + 1)
for m in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, N+1):
    if visit[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)