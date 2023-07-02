n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_dict = {}
for i in a:
    a_dict[i] = 1

b_dict = {}
for i in b:
    b_dict[i] = 1

a_cnt = 0
for i in a:
    if i in b_dict.keys():
        a_cnt += 1
a_cnt = n - a_cnt

b_cnt = 0
for i in b:
    if i in a_dict.keys():
        b_cnt += 1
b_cnt = m - b_cnt

print(a_cnt + b_cnt)