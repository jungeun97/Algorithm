from collections import deque

def bfs():
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        if x == r2 and y == c2:
            return arr[x][y]
            break
        for (nx, ny) in (x-2, y-1), (x-2, y+1), (x, y-2), (x, y+2), (x+2, y-1), (x+2, y+1):
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])
    return -1


n = int(input())
r1, c1, r2, c2 = map(int, input().split())
arr = list([0] * n for _ in range(n))

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


for i in range(n):
    for j in range(n):
        if i == r1 and j == c1:
            print(bfs())