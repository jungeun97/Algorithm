def f(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b

n = int(input())
sik = list(input())
ysj = ['+', '-', '*', '/']
stack = []
nums = []

for _ in range(n):
    nums.append(int(input()))

for i in range(len(sik)):
    if sik[i] not in ysj:
        stack.append(nums[ord(sik[i]) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(f(a, b, sik[i]))
print('%0.2f'%stack[0])
