from collections import deque

def bfs(i):
    global cnt
    q = deque()
    q.append(i)
    visited[i] = 1
    while q:
        x = q.popleft()
        for k in [-rock[x], rock[x]]:
            ni = x + k
            if 0 <= ni < n and not visited[ni]:
                visited[ni] = 1
                cnt += 1
                q.append(ni)

n = int(input())
rock = list(map(int, input().split()))
visited = [0] * n
s = int(input()) - 1
di = [-1, 1]
cnt = 1

bfs(s)

print(cnt)