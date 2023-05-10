n = list(input())
lst = []

for i in range(len(n)):
    lst.append(int(n[i]))

lst.sort(reverse=True)
dap = ''
for i in range(len(lst)):
    dap += str(lst[i])
print(dap)