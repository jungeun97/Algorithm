r, c, w = map(int, input().split())

pascal = [[0] * (r+w-1) for _ in range(r+w-1)]
pascal[0][0] = 1
for i in range(1, r+w-1):
    for j in range(i):
        pascal[i][i] = 1
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

hap = 0
for i in range(w):
    for j in range(i+1):
        # print((i+r-1, c+j-1))
        hap += pascal[i+r-1][c+j-1]
print(hap)