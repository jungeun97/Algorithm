n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for i in range(1, 1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(arr[j])
    result.append(subset)

cnt = 0
for i in range(len(result)):
    if sum(result[i]) == s:
        cnt += 1
print(cnt)