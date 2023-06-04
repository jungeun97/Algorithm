n, score, p = map(int, input().split())
if n != 0:
    arr = list(map(int, input().split()))
    if arr[-1] >= score and n == p:
        print(-1)
    else:
        ans = n + 1
        for i in range(n):
            if arr[i] <= score:
                ans = i + 1
                break
        print(ans)
else:
    print(1)