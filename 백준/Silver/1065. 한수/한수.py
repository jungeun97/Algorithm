n = input()
cnt = 0
for i in range(1, int(n)+1):
    k = str(i)
    if i < 100:
        cnt += 1
    elif int(k[1])-int(k[0]) == int(k[2])-int(k[1]):
        cnt += 1
print(cnt)