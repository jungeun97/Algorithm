import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    global cnt
    cnt += 1
    arr[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
            dfs(nx,ny)

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for j in range(x1, x2):
        for l in range(y1, y2):
            arr[j][l] = 1

dap = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            cnt = 0
            dfs(i, j)
            dap.append(cnt)

print(len(dap))
dap.sort()
for i in range(len(dap)):
    print(dap[i], end=' ')
