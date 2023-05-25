t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(k+1):
        dp[0][i] = i

    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[n][k])
