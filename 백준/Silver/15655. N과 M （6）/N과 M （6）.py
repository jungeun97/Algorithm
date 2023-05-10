def dfs(x):
    if len(lst) == m:
        for i in lst:
            print(i, end=' ')
        print()
        return
    for i in range(x, n):
        if not num[i] in lst:
            lst.append(num[i])
            dfs(i+1)
            lst.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
lst = []
dfs(0)