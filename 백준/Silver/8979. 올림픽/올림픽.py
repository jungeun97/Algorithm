n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

olympic = sorted(arr, key=lambda x:(-x[1], -x[2], -x[3]))

dap = 0
for i in range(n):
    if olympic[i][0] == k:
        cnt = 0
        if olympic[i][1:3] in olympic:
            cnt += 1
        dap = i - cnt
print(dap)