import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(i, j):
    global cnt
    pic[i][j] = 0
    cnt += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and pic[ni][nj] == 1:
            dfs(ni, nj)

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

lst = []
for i in range(n):
    for j in range(m):
        if pic[i][j] == 1:
            cnt = 0
            dfs(i, j)
            lst.append(cnt)
            
if len(lst) == 0:
    print(0)
    print(0)
else:
    print(len(lst))
    print(max(lst))