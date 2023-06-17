n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.reverse()

answer = 0
for i in range(n):
    if k == 0:
        break
    answer += k//lst[i]
    k %= lst[i]
print(answer)
