from collections import deque

def bfs(i, j):
    q = deque()
    arr[i][j] = 0
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx, ny))


di = [1, -1, 0, 0, 1, -1, -1, 1]
dj = [0, 0, -1, 1, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)

