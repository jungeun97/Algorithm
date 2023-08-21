n = int(input())
lst = []
for _ in range(n):
    a = list(map(int, input().split()))
    lst.append(a)

lst.sort(key = lambda x : x[2], reverse=True)
ans = [[lst[0][0], lst[0][1]], [lst[1][0], lst[1][1]]]
cnt = [0] * 101

cnt[ans[0][0]] += 1
cnt[ans[1][0]] += 1

for i in range(2, n):
    if cnt[lst[i][0]] == 2:
        pass
    else:
        ans.append([lst[i][0], lst[i][1]])
        break

for i in ans:
    print(*i)