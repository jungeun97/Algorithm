def binarySearch(N, key):
    ans = 0
    start = 0
    end = n-1
    while start <= end:
        middle = (start + end) // 2
        if sang[middle] == key:
            ans = 1
            return ans
        elif sang[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return ans

n = int(input())
sang = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))

sang.sort()
for i in range(m):
    print(binarySearch(n, card[i]), end = ' ')
print()

# print(' '.join(dap))