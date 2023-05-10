import heapq as hq

n, m = map(int, input().split())
gift = list(map(int, input().split()))
kids = list(map(int, input().split()))

gifts = []
for i in gift:
    hq.heappush(gifts, -i)

flag = True
for i in kids:
    k = -hq.heappop(gifts)
    if k - i < 0:
        flag = False
        break
    hq.heappush(gifts, -(k-i))

if flag:
    print(1)
else:
    print(0)

