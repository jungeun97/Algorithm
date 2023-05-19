import sys
sys.setrecursionlimit(300000)

def dfs(v):
    for n in graph[v]:
        if visited[n] == 0:
            visited[n] = visited[v] + 1
            dfs(n)

n = int(input())
graph = [[] for _ in range(n+1)]
a, b = map(int, input().split())
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)
dfs(a)

if visited[b] > 0:
    print(visited[b])
else:
    print(-1)

