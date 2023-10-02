arr = list(list(input()) for _ in range(8))
cnt = 0
for i in range(8):
    for j in range(8):
        if i % 2:
            if j % 2:
                if arr[i][j] == 'F':
                    cnt += 1
        else:
            if not j % 2:
                if arr[i][j] == 'F':
                    cnt += 1
print(cnt)