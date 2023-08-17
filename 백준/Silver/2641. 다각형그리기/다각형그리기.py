n = int(input())
arr = list(map(int, input().split()))
rev = []
for i in arr:
    if i == 1:
        rev.append(3)
    elif i == 2:
        rev.append(4)
    elif i == 3:
        rev.append(1)
    elif i == 4:
        rev.append(2)
rev.reverse()
m = int(input())
ans = []
for _ in range(m):
    lst = list(map(int, input().split()))

    if lst == arr or lst == rev:
        ans.append(lst)
        continue

    for i in range(1, n):
        tmp = lst[i:] + lst[:i]
        if tmp == arr or tmp == rev:
            ans.append(lst)
            break

print(len(ans))
for i in ans:
    print(*i)
