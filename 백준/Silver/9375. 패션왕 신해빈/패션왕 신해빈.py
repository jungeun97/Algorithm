t = int(input())
for _ in range(t):
    n = int(input())
    type = {}
    dap = 1
    for _ in range(n):
        a, b = input().split()
        if b in type:
            type[b] += 1
        else:
            type[b] = 1
    for b in type:
        dap *= type[b] + 1
    print(dap-1)

