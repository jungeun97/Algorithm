from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        if x == want_x and y == want_y:
            return visited[x][y]
        for k in range(8):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

t = int(input())
for _ in range(t):
    l = int(input())
    now_x, now_y = map(int, input().split())
    want_x, want_y = map(int, input().split())

    d = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    visited = [[0] * l for _ in range(l)]

    print(bfs(now_x, now_y)-1)

