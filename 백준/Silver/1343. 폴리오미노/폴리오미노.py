lst = input()

lst = lst.replace('XXXX', 'AAAA')
lst = lst.replace('XX', 'BB')

if 'X' in lst:
    print(-1)
else:
    print(lst)