s = input() + ' '
ans = ''
stack = []
flag = 0
for i in range(len(s)):
    if s[i] == '<':
        flag = 1
        for _ in range(len(stack)):
            ans += stack.pop()
    stack.append(s[i])
    if s[i] == '>':
        flag = 0
        for _ in range(len(stack)):
            ans += stack.pop(0)
    if s[i] == ' ' and flag == 0:
        stack.pop()
        for _ in range(len(stack)):
            ans += stack.pop()
        ans += ' '
print(ans)
