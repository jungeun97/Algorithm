from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    # 연합 국가 구하기
    union = []
    union.append((x, y))
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if l <= abs(arr[i][j] - arr[ni][nj]) <= r:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    union.append((ni, nj))
    return union

n, l, r = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

dap = 0
while True:
    visited = [[0] * (n+1) for _ in range(n)]
    flag = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                visited[x][y] = 1
                # 연합 국가 구하기
                union = bfs(x, y)
                # 연합인 국가가 있으면
                if len(union) > 1:
                    # 인구 이동
                    flag = 1
                    hap = 0
                    for i, j in union:
                        hap += arr[i][j]
                    people = hap // len(union)
                    for i, j in union:
                        arr[i][j] = people
    if not flag:
        break
    else:
        dap += 1
print(dap)