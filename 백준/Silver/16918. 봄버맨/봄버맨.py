from collections import deque

def bfs(q, arr):
    while q:
        x, y = q.popleft()
        arr[x][y] = '.'
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == 'O':
                arr[nx][ny] = '.'

def test(t):
    global q, arr

    if t == 1:
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 'O':
                    q.append((i, j))
        # for i in arr:
        #     print(*i)

    elif t % 2 == 1:
        bfs(q, arr)
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 'O':
                    q.append((i, j))
        # for i in arr:
        #     print(*i)

    else:
        arr = [['O'] * c for _ in range(r)]


r, c, n = map(int, input().split())
arr = [list(input()) for _ in range(r)]
q = deque()
di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

for i in range(1, n+1):
    test(i)

for i in arr:
    print(''.join(i))
