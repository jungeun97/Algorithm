n = int(input())
lst = list(map(int, input().split()))
lst2 = [0] * n

lst.sort()
cnt = 0
lst2[0] = lst[0]
for i in range(1, n):
    lst2[i] = lst2[i-1] + lst[i]
for i in range(1, n):
    cnt += lst2[i]
print(cnt+lst[0])