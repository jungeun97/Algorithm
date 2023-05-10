import sys
from collections import deque

def bfs():
    while q:
        z, x, y = q.popleft()
        for k in range(6):
            nx = x + di[k]
            ny = y + dj[k]
            nz = z + dz[k]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and not visited[nz][nx][ny] and not arr[nz][nx][ny] :
                visited[nz][nx][ny]  = visited[z][x][y] + 1
                arr[nz][nx][ny]  = 1
                q.append((nz, nx, ny))


m, n, h = map(int, input().split())
arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0] * m for _ in range(n)] for _ in range(h)]
di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque()

for l in range(h):
    for i in range(n):
        for j in range(m):
            if arr[l][i][j] == 1 and not visited[l][i][j]:
                visited[l][i][j] = 1
                q.append((l, i, j))
bfs()
cnt = 0
for i in visited:
    for j in i:
        cnt = max(cnt, max(j))
for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
print(cnt-1)