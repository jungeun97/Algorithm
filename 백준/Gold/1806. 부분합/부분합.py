import sys

n, s = map(int, input().split())
lst = list(map(int, input().split()))
l, r = 0, 0
hap = 0
minV = sys.maxsize

while True:
    if hap >= s:
        minV = min(minV, r - l)
        hap -= lst[l]
        l += 1
    elif r == n:
        break
    else:
        hap += lst[r]
        r += 1

if minV == sys.maxsize:
    print(0)
else:
    print(minV)