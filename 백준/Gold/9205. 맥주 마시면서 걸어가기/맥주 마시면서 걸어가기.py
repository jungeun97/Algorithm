from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if abs(x-fex) + abs(y-fey) <= 1000:
            return 'happy'
        for k in range(n):
            if visited[k] == 0:
                if abs(x-con[k][0]) + abs(y-con[k][1]) <= 1000:
                    visited[k] = 1
                    q.append((con[k][0], con[k][1]))
    return 'sad'


t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    con = list(list(map(int, input().split())) for _ in range(n))
    fex, fey = list(map(int, input().split()))

    visited = [0] * n
    print(bfs(hx, hy))