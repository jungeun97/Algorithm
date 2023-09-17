n = input()
if int(n) < 10:
    n = '0' + n
cnt = 1
if int(n[0]) + int(n[1]) >= 10:
    tmp = n[1] + str(int(n[0]) + int(n[1]))[1]
else:
    tmp = n[1] + str(int(n[0]) + int(n[1]))

while tmp != n:
    if tmp == n:
        break
    if int(tmp[0]) + int(tmp[1]) >= 10:
        tmp = tmp[1] + str(int(tmp[0]) + int(tmp[1]))[1]
    else:
        tmp = tmp[1] + str(int(tmp[0]) + int(tmp[1]))
    cnt += 1
print(cnt)