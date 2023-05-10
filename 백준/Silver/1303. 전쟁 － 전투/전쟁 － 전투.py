def dfs(i, j, c):
    global cnt
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == c and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            cnt += 1
            dfs(ni, nj, c)

n, m = map(int, input().split())
arr = list(input() for _ in range(m))
visited = list([0]*n for _ in range(m))
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

w = 0
b = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 'W' and visited[i][j] == 0:
            visited[i][j] = 1
            cnt = 1
            dfs(i, j, 'W')
            w += cnt ** 2
        elif arr[i][j] == 'B' and visited[i][j] == 0:
            visited[i][j] = 1
            cnt = 1
            dfs(i, j, 'B')
            b += cnt ** 2

print(w, b)