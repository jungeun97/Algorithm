h, w = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for i in range(1, w-1):
    left = max(lst[:i])
    right = max(lst[i+1:])
    tmp = min(left, right)
    if lst[i] < tmp:
        cnt += tmp - lst[i]
print(cnt)