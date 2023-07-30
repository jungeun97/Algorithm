from collections import deque

def bfs():
    global cnt
    visited[r] = 1
    q = deque()
    q.append(r)
    while q:
        x = q.popleft()
        for i in sorted(graph[x], reverse=True):
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                q.append(i)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()

for v in visited[1:]:
    print(v)
