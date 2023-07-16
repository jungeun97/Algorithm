n = int(input())
a = list(map(int, input().split()))
a_lst = sorted(a)
lst = []
for i in range(n):
    idx = a_lst.index(a[i])
    lst.append(idx)
    a_lst[idx] = -1
print(*lst)