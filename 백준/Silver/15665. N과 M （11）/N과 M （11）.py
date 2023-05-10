def dfs():
    if len(lst) == m:
        for i in lst:
            print(i, end=' ')
        print()
        return
    flag = 0
    for i in range(n):
        if flag != num[i]:
            lst.append(num[i])
            flag = num[i]
            dfs()
            lst.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
lst = []
dfs()