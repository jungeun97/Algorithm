def check(i, j, n):
    if n == '<':
        return i < j
    else:
        return i > j

def dfs(num, number):
    if num == k+1:
        ans.append(number)
        return
    for i in range(10):
        if visited[i] == 0:
            if num == 0 or check(number[-1], str(i), lst[num - 1]):
                visited[i] = 1
                dfs(num+1, number+str(i))
                visited[i] = 0

k = int(input())
lst = list(input().split())

visited = [0] * 10
ans = []

dfs(0, "")
print(ans[-1])
print(ans[0])

