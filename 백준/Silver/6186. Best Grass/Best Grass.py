from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < r and 0 <= nj < c and not visited[ni][nj] and arr[ni][nj] == '#':
                visited[ni][nj] = 1
                q.append((ni, nj))

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
cnt = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == '#' and not visited[i][j]:
            bfs(i, j)
            cnt += 1
print(cnt)