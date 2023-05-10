import sys
sys.setrecursionlimit(11111)

def dfs(i, j, num):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] > num and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj, num)
    # return

n = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

arr = [list(map(int, input().split())) for _ in range(n)]

nums = [0]
for i in range(n):
    for j in range(n):
        nums.append(arr[i][j])
number = set(nums)

dap = 0
for num in number:
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > num:
                visited[i][j] = 1
                cnt += 1
                dfs(i, j, num)
    if cnt > dap:
        dap = cnt
print(dap)