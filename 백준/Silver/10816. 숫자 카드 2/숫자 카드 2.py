n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

cnt = {}
for card in cards:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1

for num in nums:
    res = cnt.get(num)
    if res == None:
        print(0, end = " ")
    else:
        print(res, end=" ")