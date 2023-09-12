a = int(input())
b = int(input())
c = int(input())
dict = {}
for i in range(10):
    dict[i] = 0
ans = str(a * b * c)
for k in ans:
    i = int(k)
    if dict[i]:
        dict[i] += 1
    else:
        dict[i] = 1
for keys in dict:
    print(dict[keys])