n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input()))
lst.reverse()
answer = 0
for i in range(n-1):
    if lst[i] <= lst[i+1]:
        answer += abs((lst[i] - 1) - lst[i+1])
        lst[i+1] = lst[i] - 1
print(answer)