def dfs(v, i):
    visited[v] = 1
    for w in graph[v]:
        if not visited[w]:
            dfs(w, i)
        elif visited[w] and w == i:
            ans.append(w)

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(1, n+1):
    graph[int(input())].append(i)

ans = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    dfs(i, i)

print(len(ans))
ans.sort()
for i in ans:
    print(i)