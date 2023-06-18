sik = input().split('-')
num = []
for i in sik:
    dap = 0
    for j in i.split('+'):
        dap += int(j)
    num.append(dap)
for i in range(1, len(num)):
    num[0] -= num[i]
print(num[0])