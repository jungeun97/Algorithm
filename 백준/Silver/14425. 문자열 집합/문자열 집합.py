n, m = map(int, input().split())
ans = 0
dict = {}
for _ in range(n):
    s = input().rstrip()
    dict[s] = 1
for _ in range(m):
    key = input().rstrip()
    if key in dict:
        ans += 1
print(ans)