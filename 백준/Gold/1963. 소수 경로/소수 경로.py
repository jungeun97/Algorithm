from collections import deque

def bfs(a, b):
    q = deque()
    q.append((a, 0))
    while q:
        x, y = q.popleft()
        if x == b:
            print(y)
            return
        for i in range(4):
            for j in range(10):
                nx = list(str(x))
                nx[i] = str(j)
                nx = int(''.join(nx))
                if 1000 <= nx and not visited[nx] and lst[nx]:
                    visited[nx] = 1
                    q.append((nx, y + 1))

def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**1/2) + 1):
        if n % i == 0:
            return False
    return True


lst = [0]
for i in range(1, 10000):
    lst.append(prime(i))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    visited = [0] * 10000
    visited[a] = 1
    bfs(a, b)