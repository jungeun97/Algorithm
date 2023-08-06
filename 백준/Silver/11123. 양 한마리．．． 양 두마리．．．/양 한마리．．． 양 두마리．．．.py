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
            if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and arr[ni][nj] == '#':
                q.append((ni, nj))
                visited[ni][nj] = 1

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == '#':
                cnt += 1
                bfs(i, j)

    print(cnt)