import sys
sys.setrecursionlimit(3000000)

def dfs(i, j):
    visited[i][j] == 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and arr[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj)

m, n = map(int, input().split())
arr = list(list(map(int, input())) for _ in range(m))
visited = list([0] * n for _ in range(m))

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

for j in range(n):
    if arr[0][j] == 0:
        dfs(0, j)

dap = 0
for l in range(n):
    dap += visited[m-1][l]
if dap > 0:
    print('YES')
else:
    print('NO')