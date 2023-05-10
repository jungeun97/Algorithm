n = int(input())
lst = []
for _ in range(n):
    a = input()
    if a not in lst:
        lst.append(a)

lst.sort(key = lambda x : (len(x), x))

for i in lst:
    print(i)