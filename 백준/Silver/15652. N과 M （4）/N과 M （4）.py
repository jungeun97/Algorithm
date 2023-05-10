def dfs(x):
    if len(lst) == m:
        for i in lst:
            print(i, end=' ')
        print()
        return
    for i in range(x, n+1):
        lst.append(i)
        dfs(i)
        lst.pop()


n, m = map(int, input().split())
lst = []
dfs(1)