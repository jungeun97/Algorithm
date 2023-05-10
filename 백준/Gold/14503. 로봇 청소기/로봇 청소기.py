n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

x, y = r, c
arr[x][y] = 9
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        d -= 1
        if d == -1:
            d = 3
        nx = x + di[d]
        ny = y + dj[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            arr[nx][ny] = 9
            cnt += 1
            x, y = nx, ny
            flag = 1
            break
    # 네 방향 모두 청소 불가능
    if not flag:
        # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다
        if arr[x-di[d]][y-dj[d]] == 1:
            break
        # 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다
        else:
            x, y = x-di[d], y-dj[d]

print(cnt)
