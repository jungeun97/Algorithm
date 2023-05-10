import sys
sys.setrecursionlimit(11111)

def dfs(i, j):
    arr[i][j] = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
            dfs(ni, nj)

t = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)
