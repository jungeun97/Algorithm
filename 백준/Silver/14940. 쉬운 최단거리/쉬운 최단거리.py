from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
visited = list([-1] * m for _ in range(n))
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end = ' ')
        else:
            print(visited[i][j], end=' ')
    print()



