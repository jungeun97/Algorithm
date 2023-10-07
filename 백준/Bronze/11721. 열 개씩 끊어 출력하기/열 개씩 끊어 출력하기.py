n = input()
word = ''
for i in n:
    if len(word) == 10:
        print(word)
        word = ''
    word += i
print(word)