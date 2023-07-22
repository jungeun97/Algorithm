n = int(input())
lst = []
length = 0
for _ in range(n):
    a = input()
    length = len(a)
    rev_a = a[::-1]
    lst.append(rev_a)

cnt = 1
for i in range(1, length):
    tmp = []
    for j in range(n):
        if lst[j-1][:i] in tmp:
            cnt += 1
            break
        else:
            tmp.append(lst[j-1][:i])
    if len(tmp) == n:
        break
print(cnt)