n = int(input())
nums = list(map(int, input().split()))
a = max(nums)
lst = []
for i in nums:
    i = i / a * 100
    lst.append(i)
print(sum(lst) / n)