from collections import defaultdict

t = int(input())
for _ in range(t):
    w = input()
    k = int(input())
    dic = defaultdict(list)
    for i in range(len(w)):
        if w.count(w[i]) >= k:
            dic[w[i]].append(i)
    minV = len(w)
    maxV = 0
    for i in dic:
        for j in range(len(dic[i]) - k + 1):
            length = dic[i][j+k-1] - dic[i][j] + 1
            minV = min(minV, length)
            maxV = max(maxV, length)

    if not dic:
        print(-1)
    else:
        print(minV, maxV)

