from collections import deque

n, k = map(int, input().split())

q = deque()
for i in range(1, n+1):
    q.append(i)
ans = []

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())
print(str(ans).replace('[', '<').replace(']', '>'))