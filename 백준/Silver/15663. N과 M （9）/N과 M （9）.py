def dfs(x):
    if len(lst) == m:
        for i in lst:
            print(i, end=' ')
        print()
        return
    flag = 0
    for i in range(n):
        if not visited[i] and flag != num[i]:
            visited[i] = 1
            lst.append(num[i])
            flag = num[i]
            dfs(x+1)
            visited[i] = 0
            lst.pop()


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
lst = []
visited=[0] * n
dfs(0)
