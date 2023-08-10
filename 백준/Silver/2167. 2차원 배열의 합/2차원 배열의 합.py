n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1

    cnt = 0
    for a in range(i, x+1):
        for b in range(j, y+1):
           cnt += arr[a][b]
    print(cnt)
