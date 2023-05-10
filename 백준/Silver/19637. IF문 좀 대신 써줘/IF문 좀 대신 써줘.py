import sys

def search(lst, c):
    start = 0
    end = n - 1
    dap = 0
    while start <= end:
        mid = (start + end) // 2
        if int(lst[mid][1]) >= c:
            end = mid - 1
            dap = mid
        else:
            start = mid + 1
    return dap

n, m = map(int, sys.stdin.readline().split())
lst = [sys.stdin.readline().split() for _ in range(n)]

char = []
for _ in range(m):
    c = int(sys.stdin.readline())
    print(lst[search(lst, c)][0])
