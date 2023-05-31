def f(cnt, idx):
    if cnt == l:
        vo, co = 0, 0
        for i in key:
            if i in vowel:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >=2:
            print(''.join(key))
        return

    for i in range(idx, c):
        key.append(lst[i])
        f(cnt+1, i+1)
        key.pop()

l, c = map(int, input().split())
lst = list(input().split())
lst.sort()
vowel = ['a', 'i', 'u', 'e', 'o']
key = []
f(0, 0)