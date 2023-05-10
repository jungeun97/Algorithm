def dfs(x):
    if len(lst) == m:
        for i in lst:
            print(i, end=' ')
        print()
        return
    for i in range(x, n+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)
            lst.pop()

n, m = map(int, input().split())
lst = []
dfs(1)