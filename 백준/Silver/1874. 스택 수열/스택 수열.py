n = int(input())
cnt = 1
stack = []
ans = []
flag = 0
for i in range(n):
    a = int(input())
    while cnt <= a:
        stack.append(cnt)
        ans.append('+')
        cnt += 1

    if stack[-1] == a:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        flag = 1
        break
if not flag:
    for i in ans:
        print(i)