h, w, x, y = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h+x)]
a = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        a[i][j] = b[i][j]

for i in range(x, h):
    for j in range(y, w):
        a[i][j] = b[i][j] - a[i-x][j-y]

for i in range(h):
    print(*a[i])

