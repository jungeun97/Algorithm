from collections import deque

def bfs(i, j, k):
    q = deque()
    q.append((i, j, k))
    visited[i][j][k] = 1
    while q:
        x, y, z = q.popleft()
        for a in range(6):
            nx = x + dk[a]
            ny = y + di[a]
            nz = z + dj[a]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c and not visited[nx][ny][nz]:
                if arr[nx][ny][nz] == '.' :
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q.append((nx, ny, nz))
                if arr[nx][ny][nz] == 'E':
                    print("Escaped in {0} minute(s).".format(visited[x][y][z]))
                    return
    print('Trapped!')



while True:
    l, r, c = map(int, input().split())

    di = [1, -1, 0, 0, 0, 0]
    dj = [0, 0, 1, -1, 0, 0]
    dk = [0, 0, 0, 0, -1, 1]

    if l == 0 and r == 0 and c == 0:
        break

    arr = list(list([] for _ in range(r)) for _ in range(l))

    for i in range(l):
        arr[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()

    visited = [[[0] * c for _ in range(r)] for _ in range(l)]

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k] == 'S':
                    bfs(i, j, k)
