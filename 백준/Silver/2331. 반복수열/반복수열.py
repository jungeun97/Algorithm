a, p = map(int, input().split())
d = [a]

while True:
    tmp = 0
    for i in str(d[-1]):
        tmp += int(i) ** p

    if tmp in d:
        d = d[:d.index(tmp)]
        break

    d.append(tmp)
print(len(d))
