def dfs():
    if len(lst) == m:
        for i in lst:
            print(i, end=' ')
        print()
        return
    for i in num:
        lst.append(i)
        dfs()
        lst.pop()


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
lst = []
dfs()