n, m = map(int, input().split())
hear = []
see = []
for  _ in range(n):
    a = input()
    hear.append(a)
for _ in range(m):
    a = input()
    see.append(a)

dap = set(hear) & set(see)
dap1 = sorted(list(dap))


print(len(dap1))
for i in dap1:
    print(i)