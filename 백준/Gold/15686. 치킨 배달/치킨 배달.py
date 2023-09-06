from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chi = []
zip = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            zip.append((i, j))
        elif arr[i][j] == 2:
            chi.append((i, j))
ans = []
for i in combinations(chi, m):
    hap = 0
    for l in zip:
        dist = []
        for j in i:
            r, c = j[0], j[1]
            dist.append(abs(r - l[0]) + abs(c - l[1]))
        minV = min(dist)
        hap += minV
    ans.append(hap)
print(min(ans))