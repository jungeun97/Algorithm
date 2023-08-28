n = int(input())
lst = list(list(input()) for _ in range(n))
ans = ''
for i in range(len(lst[0])):
    tmp = lst[0][i]
    flag = 0
    for j in range(1, n):
        if lst[j][i] != tmp:
            ans += '?'
            flag = 1
            break
    if not flag:
        ans += tmp
print(ans)
