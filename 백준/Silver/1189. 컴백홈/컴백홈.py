def dfs(i, j):
    global cnt
    if i == 0 and j == c - 1:
        if visited[i][j] == k:
            cnt += 1
        return
    for l in range(4):
        ni = i + di[l]
        nj = j + dj[l]
        if 0 <= ni < r and 0 <= nj < c and not visited[ni][nj] and arr[ni][nj] != 'T':
            visited[ni][nj] = visited[i][j] + 1
            dfs(ni, nj)
            visited[ni][nj] = 0

r, c, k = map(int, input().split())
arr = list(list(input()) for _ in range(r))
visited = list([0] * c for _ in range(r))
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
visited[r-1][0] = 1
cnt = 0
dfs(r-1, 0)
print(cnt)