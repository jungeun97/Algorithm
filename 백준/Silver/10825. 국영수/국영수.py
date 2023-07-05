n = int(input())
lst = []
for _ in range(n):
    a, b, c, d = input().split()
    lst.append((a, int(b), int(c), int(d)))
lst.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
for i in lst:
    print(i[0])