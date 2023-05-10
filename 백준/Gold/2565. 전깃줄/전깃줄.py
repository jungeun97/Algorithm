n = int(input())
line = []
dp = [1] * n
for _ in range(n):
    a1, b1 = map(int, input().split())
    line.append((a1, b1))
line.sort()

for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))

