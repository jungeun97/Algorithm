n = int(input())

lst =  []
for i in range(666, 10000*666):
    if '666' in str(i):
        lst.append(i)
print(lst[n-1])