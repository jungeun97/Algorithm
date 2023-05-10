def dfs(x):
    if len(lst) == m:
        for i in lst:
            print(i, end=' ')
        print()
        return
    flag = 0
    for i in range(x, n):
        if flag != num[i]:
            lst.append(num[i])
            flag = num[i]
            dfs(i)
            lst.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
lst = []
dfs(0)