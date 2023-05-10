k, n = map(int, input().split())
sun = []
for _ in range(k):
    a = int(input())
    sun.append(a)
sun.sort()

start = 1
end = max(sun)

while start <= end:
    mid = (start + end) // 2
    dap = 0
    for i in sun:
        dap += i // mid

    if dap >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)