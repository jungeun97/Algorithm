def solve(n):
    global ans
    if n > N:
        return

    if n == N:
        ans += 1

    else:
        op = [n + 1, n + 2, n + 3]
        for x in op:
            solve(x)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = 0
    solve(0)
    print(ans)
