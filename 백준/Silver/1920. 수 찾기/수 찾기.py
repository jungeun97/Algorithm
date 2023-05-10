def search(v):
    s = 0
    e = n-1
    flag = 0
    while s <= e:
        mid = (s + e) // 2
        if v < arr[mid]:
            e = mid - 1
        elif v > arr[mid]:
            s = mid + 1
        elif v == arr[mid]:
            flag = 1
            return 1
    if not flag:
        return 0


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    print(search(i))

