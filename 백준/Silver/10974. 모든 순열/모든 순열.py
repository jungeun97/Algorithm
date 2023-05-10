def perm(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append([arr[i]]+p)
    return result

n = int(input())
arr = []
for i in range(1, n+1):
    arr.append(i)
ans = perm(arr, n)
for i in range(len(ans)):
    print(' '.join(map(str, ans[i])))
print()