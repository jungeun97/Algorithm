t = int(input())
for _ in range(t):
    n = int(input())
    sticker = list([0] + list(map(int, input().split())) for _ in range(2))
    dp = [[0] * (n+1) for _ in range(2)]
    ans = 0

    if len(sticker[0]) == 1:
        ans = max(sticker[0][0], sticker[1][0])
        print(ans)
    else:
        dp[0][1] = sticker[0][1]
        dp[1][1] = sticker[1][1]

        for i in range(2, n+1):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]

        print(max(dp[0][-1], dp[1][-1]))

