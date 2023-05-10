n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(n):
    hap = 0
    for j in range(i, n):
        hap += arr[j]
        if hap == m:
            cnt += 1
            break
        if hap > m:
            break
print(cnt)