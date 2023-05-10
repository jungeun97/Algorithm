n, k = map(int, input().split())
room = [[0] * 2 for _ in range(7)]

for _ in range(n):
    s, y = map(int, input().split())
    room[y][s] += 1

cnt = 0
for i in range(1, 7):
    for j in range(2):
        while room[i][j] > 0:
            if 0 < room[i][j]:
                cnt += 1
                room[i][j] -= k
print(cnt)
