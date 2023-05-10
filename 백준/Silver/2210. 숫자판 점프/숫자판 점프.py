def dfs(i, j, num):
    if len(num) == 6:
        if num not in dap:
            dap.append(num)
        return
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(ni, nj, num + arr[ni][nj])

arr = list(list(map(str, input().split())) for _ in range(5))
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

num = ''
cnt = 0
dap = []
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
print(len(dap))