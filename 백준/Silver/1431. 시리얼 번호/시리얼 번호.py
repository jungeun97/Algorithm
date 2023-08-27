n = int(input())
lst = []
for _ in range(n):
    a = input()
    lst.append(a)
lst.sort(key = lambda x : len(x))
dict = {}
for i in lst:
    cnt = 0
    for j in i:
        if j.isdigit():
            cnt += int(j)
    dict[i] = cnt
lst.sort(key = lambda x : (len(x), dict[x], x))
for i in lst:
    print(i)