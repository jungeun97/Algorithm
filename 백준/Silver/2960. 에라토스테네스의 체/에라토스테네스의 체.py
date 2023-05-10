n, k = map(int, input().split())

lst = []
for i in range(2, n+1):
    lst.append(i)
cnt = 0
while cnt < k:
    a = min(lst)
    lst.remove(a)
    cnt += 1
    if cnt == k:
        dap = a
        break
    for i in lst:
        if i % a == 0:
            lst.remove(i)
            cnt += 1
            if cnt == k:
                dap = i
                break
print(dap)