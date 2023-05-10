n, k = map(int, input().split())

lst = list(input())
for i in range(n):
    flag = 0
    if lst[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n and lst[j] == 'H':
                lst[j] = 0
                flag = 1
            if flag == 1:
                break

cnt = 0
for i in lst:
    if i == 0:
        cnt += 1
print(cnt)