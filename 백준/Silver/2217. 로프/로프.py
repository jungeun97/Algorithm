n = int(input())
lst = []
for _ in range(n):
    a = int(input())
    lst.append(a)
lst.sort(reverse=True)
dap = []
for i in range(n):
    dap.append(lst[i] * (i+1))
print(max(dap))