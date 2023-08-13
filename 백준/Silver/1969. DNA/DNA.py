n, m = map(int, input().split())
arr = []
for _ in range(n):
    a = list(input())
    arr.append(a)

cnt, hap = 0, 0
ans = ''
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if arr[j][i] == 'A':
            a += 1
        elif arr[j][i] == 'C':
            c += 1
        elif arr[j][i] == 'G':
            g += 1
        elif arr[j][i] == 'T':
            t += 1
    if max(a, c, g, t) == a:
        ans += 'A'
        hap += c + g + t
    elif max(a, c, g, t) == c:
        ans += 'C'
        hap += a + g + t
    elif max(a, c, g, t) == g:
        ans += 'G'
        hap += a + c+ t
    elif max(a, c, g, t) == t:
        ans += 'T'
        hap += a + c + g
print(ans)
print(hap)