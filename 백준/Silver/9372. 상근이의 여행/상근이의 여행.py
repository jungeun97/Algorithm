def dfs(idx, cnt):
    visit[idx] = 1
    for i in arr[idx]:
        if visit[i] == 0:
            cnt = dfs(i, cnt+1)
    return cnt

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    visit = [0] * (n+1)
    result = dfs(1, 0)
    print(result-1)

