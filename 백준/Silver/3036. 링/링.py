def gcd(a, b):
    while b != 0:
        remain = a % b
        a = b
        b = remain
    return a

n = int(input())
lst = list(map(int, input().split()))
for i in range(1, n):
    num = gcd(lst[0], lst[i])
    print('%d/%d'%(lst[0]//num, lst[i]//num))