n = int(input())
name = {}
b = 0
for _ in range(n):
    a = input()
    if a == 'ENTER':
        b += len(name)
        name = {}

    else:
        if a in name.keys():
            name[a] += 1
        else:
            name[a] = 1
print(len(name) + b)