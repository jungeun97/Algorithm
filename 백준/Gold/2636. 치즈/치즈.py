from collections import deque

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    cnt += 1
    return cnt




n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

time = 0
tmp = 0
while True:
    time += 1
    visited = [[0] * m for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break
    tmp = cnt

print(time-1)
print(tmp)