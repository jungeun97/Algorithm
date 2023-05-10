import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    for i in graph[n]:
        if not lst[i]:
            lst[i] = n
            dfs(i)

N = int(input())
graph = [[] for _ in range(N+1)]
lst = [0] * (N + 1)
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
# print(graph)
# print(lst)
for i in range(2, N+1):
    print(lst[i])