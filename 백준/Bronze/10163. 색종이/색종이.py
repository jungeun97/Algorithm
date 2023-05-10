n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for k in range(n):
    x, y, w, h = map(int, input().split())
    for i in range(y, y+h):
        for j in range(x, x+w):
            arr[i][j] = k+1


for k in range(1, n+1):
    hap = 0
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == k:
                hap += 1
    print(hap)
