from itertools import permutations

n = int(input())
num = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))
for _ in range(n):
    tmp, strike, ball = map(int, input().split())
    tmp = list(str(tmp))
    cnt = 0

    for i in range(len(num)):
        s = b = 0
        i -= cnt
        for j in range(3):
            if num[i][j] == tmp[j]:
                s += 1
            elif tmp[j] in num[i]:
                b += 1
        if (s != strike) or (b != ball):
            num.remove(num[i])
            cnt += 1
print(len(num))