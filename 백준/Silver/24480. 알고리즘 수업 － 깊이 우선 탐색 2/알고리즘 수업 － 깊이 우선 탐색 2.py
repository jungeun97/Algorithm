from sys import stdin,setrecursionlimit
input = stdin.readline

def dfs(v):
    global cnt
    visited[v] = cnt
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)


n, m, r = map(int, input().split())
setrecursionlimit(n+10)
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)
dfs(r)

for i in visited[1:]:
    print(i)

