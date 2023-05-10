import sys
sys.setrecursionlimit(10000)

def dfs(i, j, a):
    visited[i][j] = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] == a:
            dfs(ni, nj, a)

def dfs2(i, j, a):
    visited2[i][j] = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and visited2[ni][nj] == 0 and arr[ni][nj] == a:
            dfs2(ni, nj, a)

n = int(input())
arr = list(list(input()) for _ in range(n))
visited = list([0] * n for _ in range(n))
visited2 = list([0] * n for _ in range(n))

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

r_cnt = 0
g_cnt = 0
b_cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R' and visited[i][j] == 0:
            r_cnt += 1
            dfs(i, j, 'R')
        elif arr[i][j] == 'G' and visited[i][j] == 0:
            g_cnt += 1
            dfs(i, j, 'G')
        elif arr[i][j] == 'B' and visited[i][j] == 0:
            b_cnt += 1
            dfs(i, j, 'B')
x_cnt = r_cnt + g_cnt + b_cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

rr_cnt = 0
bb_cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R' and visited2[i][j] == 0:
            rr_cnt += 1
            dfs2(i, j, 'R')
        elif arr[i][j] == 'B' and visited2[i][j] == 0:
            bb_cnt += 1
            dfs2(i, j, 'B')
o_cnt = rr_cnt + bb_cnt
print(x_cnt, o_cnt)
