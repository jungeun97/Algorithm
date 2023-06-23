import itertools

n, k = map(int, input().split())
a = list(map(int, input().split()))
lst = list(itertools.permutations(a, n))

cnt = 0

for i in lst:
    flag = 1
    muscle = 500
    for j in i:
        muscle -= k
        muscle += j
        if muscle < 500:
            flag = 0
            break
    if flag:
        cnt += 1
print(cnt)