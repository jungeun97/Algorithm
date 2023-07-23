n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
sero = garo = 0

# 행
for i in range(n):
    a = ''
    for j in range(m):
        if arr[i][j] == '-':
            if arr[i][j] != a:
                sero += 1
        a = arr[i][j]

# 열
for j in range(m):
    a = ''
    for i in range(n):
        if arr[i][j] == '|':
            if arr[i][j] != a:
                garo += 1
        a = arr[i][j]

print(garo+sero)