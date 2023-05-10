from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m:
                if bing[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif bing[nx][ny] == 0:
                    melting[x][y] += 1
    return 1

n, m = map(int, input().split())
bing = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

dap = 0
check = False

while True:

    visited = [[0] * m for _ in range(n)]
    melting = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(1, n):
        for j in range(1, m):
            if bing[i][j] != 0 and not visited[i][j]:
                cnt += bfs(i, j)
    for i in range(n):
        for j in range(m):
           if bing[i][j] != 0:
                bing[i][j] -= melting[i][j]
                if bing[i][j] < 0:
                    bing[i][j] = 0

    if cnt == 0:
        break
    if cnt >= 2:
        check = True
        break

    dap += 1

if check:
    print(dap)
else:
    print(0)