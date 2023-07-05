import sys
from math import gcd

n = int(input())
a = int(input())
tree = []
for _ in range(n-1):
    b = int(input())
    tree.append(b - a)
    a = b

g = tree[0]
for i in range(1, len(tree)):
    g = gcd(g, tree[i])

cnt = 0
for i in tree:
    cnt += i // g - 1
print(cnt)