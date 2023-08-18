n = int(input())
sub = []
for _ in range(n):
    lst = list(map(int, input().split()))
    sub.append(set(lst[1:]))

m = int(input())
student = []
for _ in range(m):
    arr = list(map(int, input().split()))
    student.append(set(arr[1:]))

ans = []
for i in student:
    cnt = 0
    for j in sub:
        if j.intersection(i) == j:
            cnt += 1
    print(cnt)