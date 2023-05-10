n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))
time = sorted(lst, key = lambda x : (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]
print(cnt)