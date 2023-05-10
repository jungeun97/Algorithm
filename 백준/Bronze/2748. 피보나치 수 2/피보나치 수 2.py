n = int(input())

lst = [0] * (n+1)
lst[0] = 0
lst[1] = 1
for i in range(2, n+1):
    lst[i] = lst[i-2] + lst[i-1]
print(lst[n])