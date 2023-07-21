n = int(input())
lst = [input() for _ in range(n)]
lst.sort()
cnt = 0
for i in range(n):
    flag = 0
    for j in range(i+1, n):
        # if lst[i][0] == lst[j][0]:
        if lst[i] in lst[j][0:len(lst[i])]:
            flag = 1
            break
    if not flag:
        cnt += 1
print(cnt)