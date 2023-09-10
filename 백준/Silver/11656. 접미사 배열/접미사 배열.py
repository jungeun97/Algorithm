s = input()
lst = [s]
while len(s) > 1:
    s = s[1:]
    lst.append(s)
lst.sort()
for i in lst:
    print(i)