num2 = int(input())
num = input()
lst = []
for i in num:
    a = int(i) * num2
    lst.append(a)
lst.reverse()
for i in lst:
    print(i)
for i in range(1, len(lst)):
    lst[i] *= (10 ** i)
print(sum(lst))
