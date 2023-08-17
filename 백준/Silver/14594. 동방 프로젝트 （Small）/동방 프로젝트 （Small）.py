n = int(input())
m = int(input())
lst = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    for i in range(x, y):
        lst[i] = 1
print(lst.count(0) -1)