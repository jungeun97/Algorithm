import sys
from collections import deque

def bfs(i, j):
    maxV = 0
    visited = list([0] * m for _ in range(n))
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 'L' and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                maxV = max(maxV, visited[nx][ny])
    return maxV - 1

n, m = map(int, input().split())
arr = list(list(input()) for _ in range(n))


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

dap = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            dap = max(dap, bfs(i, j))

print(dap)