import sys
sys.setrecursionlimit(2000)

def dfs(v):
    visit[v] = 1
    if visit[lst[v]] == 0:
        dfs(lst[v])

T = int(input())
for t in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    visit = [0] * (N+1)

    cnt = 0
    for i in range(1, N+1):
        if visit[i] == 0:
            dfs(i)
            cnt += 1
    print(cnt)
