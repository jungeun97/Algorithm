n = int(input())
lst = list(map(int, input().split()))

s = 0
e = n-1
ans = abs(lst[s] + lst[e])
s_idx = s
e_idx = e
while s < e:
    if abs(lst[s] + lst[e]) < ans:
        s_idx = s
        e_idx = e
        ans = abs(lst[s] + lst[e])

        if ans == 0:
            break

    if lst[s] + lst[e] < 0:
        s += 1
    else:
        e -= 1

print(lst[s_idx], lst[e_idx])
