def move(i):
    if i == 1:
        dice[0], dice[1], dice[4], dice[5] = f, e, a, b
    elif i == 2:
        dice[0], dice[1], dice[4], dice[5] = e, f, b, a
    elif i == 3:
        dice[2], dice[3], dice[4], dice[5] = e, f, d, c
    elif i == 4:
        dice[2], dice[3], dice[4], dice[5] = f, e, c, d

n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0] * 6
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

for k in order:
    nx = x + di[k-1]
    ny = y + dj[k-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    move(k)

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[5]
    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0

    x, y = nx, ny
    print(dice[4])