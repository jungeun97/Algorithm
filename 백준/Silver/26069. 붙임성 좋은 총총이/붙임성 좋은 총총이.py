n = int(input())
flag = 0
dance = set()
for _ in range(n):
    a, b = input().split()
    if a == 'ChongChong':
        dance.add(b)
    if b == 'ChongChong':
        dance.add(a)
    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)
print(len(dance))