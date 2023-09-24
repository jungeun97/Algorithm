word = input()
word = word.lower()
dict = {}

for i in word:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1
cnt = 0
ans = ''
for i in dict:
    if dict[i] == max(dict.values()):
        cnt += 1
        ans = i
if cnt > 1:
    print("?")
else:
    print(ans.upper())