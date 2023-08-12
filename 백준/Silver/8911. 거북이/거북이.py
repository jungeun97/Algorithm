t = int(input())
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
for _ in range(t):
    x, y = 0, 0
    k = 0
    minX, minY, maxX, maxY = 0, 0, 0, 0
    turtle = list(input())
    for i in turtle:
        if i == 'F':
            x += di[k]
            y += dj[k]
        elif i == 'B':
            x -= di[k]
            y -= dj[k]
        elif i == 'L':
            if k == 3:
                k = 0
            else:
                k += 1
        elif i == 'R':
            if k == 0:
                k = 3
            else:
                k -= 1
        minX = min(minX, x)
        minY = min(minY, y)
        maxX = max(maxX, x)
        maxY = max(maxY, y)

    print(abs(maxX - minX) * abs(maxY - minY))

