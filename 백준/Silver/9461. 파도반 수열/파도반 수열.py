
t = int(input())
for _ in range(t):
    n = int(input())
    p = [0 for _ in range(101)]
    p[1] = 1
    p[2] = 1
    p[3] = 1
    for i in range(4, n+1):
        p[i] = p[i-3] + p[i-2]
    print(p[n])