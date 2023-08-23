import copy

r, c = map(int, input().split())
m = list(list(input()) for _ in range(r))
nm = copy.deepcopy(m)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
for i in range(r):
    for j in range(c):
        if m[i][j] == 'X':
            cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if r <= ni or ni < 0 or c <= nj or nj < 0:
                    cnt += 1
                else:
                    if m[ni][nj] == '.':
                        cnt += 1
            if cnt >= 3:
                nm[i][j] = '.'

row = []
col = []
for a in range(r):
    for b in range(c):
        if nm[a][b] == 'X':
            row.append(a)
            col.append(b)

if row:
    sr = min(row)
    er = max(row)
    sc = min(col)
    ec = max(col)
    for i in range(sr, er + 1):
        for j in range(sc, ec + 1):
            print(nm[i][j], end='')
        print()
# else:
#     print('X')