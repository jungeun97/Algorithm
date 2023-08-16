n, q = map(int, input().split())
lst = list(map(int, input().split()))
for _ in range(q):
    a, b = map(int, input().split())
    if b - 1 < a:
        print(0)
    else:
        cnt = 0
        for i in range(a-1, b-1):
            cnt += abs(lst[i+1] - lst[i])
        print(cnt)