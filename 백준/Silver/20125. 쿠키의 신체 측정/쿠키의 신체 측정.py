n = int(input())
arr = list(list(input()) for _ in range(n))
flag = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '*':
            simX, simY = i+1, j
            flag = 1
            break
    if flag:
        break
leftA, rightA, w, leftL, rightL = 0, 0, 0, 0, 0
for i in range(0, simY):
    if arr[simX][i] == '*':
        leftA += 1
for i in range(simY+1, n):
    if arr[simX][i] == '*':
        rightA += 1
for i in range(simX+1, n):
    if arr[i][simY] == '*':
        w += 1
for i in range(simX+w+1, n):
    if arr[i][simY-1] == '*':
        leftL += 1
for i in range(simX+w+1, n):
    if arr[i][simY+1] == '*':
        rightL += 1
print(simX + 1, simY + 1)
print(leftA, rightA, w, leftL, rightL)