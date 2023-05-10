n = int(input())
lst = []
for _ in range(n):
    ex = input()
    num = []
    eng = []
    for i in range(len(ex)):
        if ex[i].isdigit():
            num.append(ex[i])
            if i == len(ex)-1:
                ans = ''.join(num)
                num.clear()
                lst.append(int(ans))

        else:
            eng.append(ex[i])
            if len(num):
                ans = ''.join(num)
                num.clear()
                lst.append(int(ans))

lst.sort()
for i in lst:
    print(i)