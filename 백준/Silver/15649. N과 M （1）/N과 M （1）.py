import itertools

n, m = map(int, input().split())

num = [i for i in range(1, n+1)]
lst = itertools.permutations(num, m)

for i in lst:
    for j in i:
        print(j, end=' ')
    print()