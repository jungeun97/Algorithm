n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
result = []

cnt = 0
for i in range(n-7):
    for j in range(m-7):
        index1 = 0
        index2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if arr[a][b] != 'B':
                        index1 += 1
                    if arr[a][b] != 'W':
                        index2 += 1
                else:
                    if arr[a][b] != 'W':
                        index1 += 1
                    if arr[a][b] != 'B':
                        index2 += 1
        result.append(index1)
        result.append(index2)
print(min(result))