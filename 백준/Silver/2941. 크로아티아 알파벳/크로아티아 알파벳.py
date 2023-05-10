word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in croatia:
    cnt += word.count(i)
    word = word.replace(i, ' ')

word = word.replace(' ', '')
cnt += len(word)
print(cnt)