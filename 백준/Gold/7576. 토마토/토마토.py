from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and not arr[nx][ny]:
                arr[nx][ny] = 1
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            q.append((i, j))
bfs()
for i in visited:
    cnt = max(cnt, max(i))
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
print(cnt - 1)

