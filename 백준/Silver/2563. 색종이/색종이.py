n = int(input())
arr = [[0] * 101 for _ in range(101)]
for _ in range(n):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)