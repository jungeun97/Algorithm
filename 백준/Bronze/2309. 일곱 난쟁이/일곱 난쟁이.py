small = []
for _ in range(9):
    h = int(input())
    small.append(h)
hap = 0
result = []
for i in range(1, (1<<9)):
    subset = []
    for j in range(0, 9):
        if i & (1 << j):
            subset.append(small[j])
    if sum(subset) == 100 and len(subset) == 7:
        result = subset
        break
dap = result.sort()
for i in range(7):
    print(result[i])
