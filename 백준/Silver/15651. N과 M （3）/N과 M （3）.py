def dfs(x):
    if len(lst) == m:
        for i in lst:
            print(i, end=' ')
        print()
        return
    for i in range(1, n+1):
        lst.append(i)
        dfs(x+1)
        lst.pop()

n, m = map(int, input().split())
lst = []
dfs(1)