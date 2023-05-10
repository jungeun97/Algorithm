n = int(input())
books = []
for i in range(n):
    book = input()
    books.append(book)

maxV = 0
maxbook = books[0]
for i in range(n):
    cnt = 0
    for j in range(n):
        if books[j] == books[i]:
            cnt += 1
            if maxV < cnt:
                maxV = cnt
                maxbook = books[i]
            if maxV == cnt:
                if maxbook > books[i]:
                    maxbook = books[i]
print(maxbook)