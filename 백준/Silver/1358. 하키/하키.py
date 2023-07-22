w, h, x, y, p = map(int, input().split())
cnt = 0
for _ in range(p):
    xx, yy = map(int, input().split())
    if x <= xx <= x + w:
        if y <= yy <= y + h:
            cnt += 1
            continue
    d1 = ((xx-x) ** 2 + (yy-(y+h/2)) ** 2) ** 0.5
    d2 = ((xx-(x+w)) ** 2 + (yy-(y+h/2))**2) ** 0.5
    if d1 <= h/2 or d2 <= h/2:
        cnt += 1

print(cnt)
