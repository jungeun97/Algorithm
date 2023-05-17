def dfs(i, j, cnt):
    global ans
    ans = max(ans, cnt)
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < r and 0 <= nj < c and not arr[ni][nj] in visited:
            visited.add(arr[ni][nj])
            dfs(ni, nj, cnt + 1)
            visited.remove(arr[ni][nj])


r, c = map(int, input().split())
arr = list(list(input()) for _ in range(r))
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
cnt = 0
ans = 0
visited = set()
visited.add(arr[0][0])
dfs(0, 0, 1)
print(ans)
