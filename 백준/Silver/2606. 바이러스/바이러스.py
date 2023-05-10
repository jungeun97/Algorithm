def dfs(v):
    visit[v] = 1
    for i in graph[v]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i)
    return visit

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visit = [0] * (N + 1)
for m in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = sum(dfs(1)) - 1
print(ans)


