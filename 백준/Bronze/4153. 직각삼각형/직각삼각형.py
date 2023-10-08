while True:
    lst = []
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.sort()
    if (lst[0] * lst[0]) + (lst[1] * lst[1]) == lst[2] * lst[2]:
        print('right')
    else:
        print('wrong')