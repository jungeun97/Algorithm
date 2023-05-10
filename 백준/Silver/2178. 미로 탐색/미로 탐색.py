from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return visited
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and miro[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

n, m = map(int, input().split())
miro = list(list(map(int, input())) for _ in range(n))
visited = list([0] * m for _ in range(n))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

bfs(0, 0)
print(visited[n-1][m-1])