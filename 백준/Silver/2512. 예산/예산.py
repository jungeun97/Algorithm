n = int(input())
money = list(map(int, input().split()))
total = int(input())

s = 0
e = max(money)

while s <= e:
    mid = (s + e) // 2
    hap = 0
    for i in money:
        if i < mid:
            hap += i
        else:
            hap += mid

    if hap > total:
        e = mid - 1
    else:
        s = mid + 1

print(e)