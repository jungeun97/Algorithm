h, w = map(int, input().split())
arr = list(list(input()) for _ in range(h))
for i in range(h):
    flag = 0
    cnt = 1
    for j in range(w):
        if flag:
            if arr[i][j] == '.':
                arr[i][j] = cnt
                cnt += 1
            else:
                arr[i][j] = 0
                cnt = 1
        else:
            if arr[i][j] == 'c':
                arr[i][j] = 0
                flag = 1
            else:
                arr[i][j] = -1

for i in arr:
    print(*i)