n = int(input())
i = n // 4
na = n % 4
if na > 0:
    i += 1
a = 'long ' * i
a += 'int'
print(a)
