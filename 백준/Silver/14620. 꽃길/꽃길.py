import sys
sys.setrecursionlimit(11111)

def check(i, j):
    cnt = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and garden[ni][nj] == 0:
            cnt += 1
    if cnt == 4:
        return True

def dfs(i, j, total, num):
    global minV
    if num == 3:
        minV = min(minV, total)
        return
    for i in range(1, n-1):
        for j in range(1, n-1):
            if check(i, j):
                garden[i][j] = 1
                cost = money[i][j]
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    garden[ni][nj] = 1
                    cost += money[ni][nj]
                dfs(ni, nj, total + cost, num+1)
                garden[i][j] = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    garden[ni][nj] = 0

n = int(input())
money = [list(map(int, input().split())) for _ in range(n)]
garden = [[0] * n for _ in range(n)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

minV = 11111
dfs(0, 0, 0, 0)
print(minV)