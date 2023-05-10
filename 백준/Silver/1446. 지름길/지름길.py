n, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [i for i in range(d+1)]

for i in range(d+1):
    if i > 0:
        # 지름길 거리와 고속도로로 간 거리 비교
        dp[i] = min(dp[i], dp[i-1]+1)
    for s, e, l in arr:
        if i == s and e <= d and dp[i]+l < dp[e]:
            dp[e] = dp[i]+l
print(dp[d])