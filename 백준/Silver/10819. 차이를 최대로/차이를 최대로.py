from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

per = permutations(arr)
ans = 0

for i in per:
    # print(i)
    s = 0
    for j in range(len(i) - 1):
        s += abs(i[j]-i[j+1])
    if s > ans:
        ans = s
print(ans)