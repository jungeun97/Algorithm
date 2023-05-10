n, x = map(int, input().split())
visitors = list(map(int, input().split()))

maxV = sum(visitors[:x])
value = maxV
cnt = 1
for i in range(x, n):
    value -= visitors[i-x]
    value += visitors[i]
    if value > maxV:
        maxV = value
        cnt = 1
    elif value == maxV:
        cnt += 1
if maxV == 0:
    print('SAD')
else:
    print(maxV)
    print(cnt)