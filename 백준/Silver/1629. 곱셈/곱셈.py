def dac(a, b):
    if b == 1:
        return a % c
    else:
        temp = dac(a, b // 2)
        if not b % 2:
            return temp * temp % c
        else:
            return temp * temp * a % c

a, b, c = map(int, input().split())
print(dac(a, b))