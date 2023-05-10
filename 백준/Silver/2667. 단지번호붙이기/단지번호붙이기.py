from collections import deque

def bfs(i, j):
    global cnt
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt + 1

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

dap = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 0
            if visited[i][j] == 0:
                dap.append(bfs(i, j))
print(len(dap))
dap.sort()
for i in dap:
    print(i)