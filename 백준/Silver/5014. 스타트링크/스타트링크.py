from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        x = q.popleft()
        if x == g:
            return count[g]
        for i in (x-d, x+u):
            if 0 < i <= f and not visited[i]:
                visited[i] = 1
                count[i] = count[x] + 1
                q.append(i)
    if count[g] == 0:
        return "use the stairs"

f, s, g, u, d = map(int, input().split())
visited = [0] * (f+1)
count = [0] * (f+1)
print(bfs(s))
