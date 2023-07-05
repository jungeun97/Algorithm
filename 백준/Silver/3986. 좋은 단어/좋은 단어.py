n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    stack = []
    for i in word:
        if not stack:
            stack.append(i)
        else:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        cnt += 1
print(cnt)
