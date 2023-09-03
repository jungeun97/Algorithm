from collections import deque
def bfs(i, j):
    visited[i][j] = 0
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if miro[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    print(visited[n-1][m-1])



m, n = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]
bfs(0, 0)
# print(visited[n-1][m-1])