from collections import deque

def bfs():
    global cnt
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and not arr[ni][nj] == 'X':
                q.append((ni, nj))
                visited[ni][nj] = 1
                if arr[ni][nj] == 'P':
                    cnt += 1

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            bfs()
if not cnt:
    print('TT')
else:
    print(cnt)

