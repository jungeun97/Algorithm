lst = []
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)
lst.append(e)
for i in range(5):
    if lst[i] < 40:
        lst[i] = 40
print(sum(lst) // 5)