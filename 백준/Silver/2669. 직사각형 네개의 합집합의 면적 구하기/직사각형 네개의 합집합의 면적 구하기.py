arr = [[0]*100 for _ in range(100)]

for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            arr[i][j] += 1

hap = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            hap += 1
print(hap)
