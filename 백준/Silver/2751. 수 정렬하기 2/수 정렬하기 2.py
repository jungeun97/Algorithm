n = int(input())
nums = []
for _ in range(n):
    a = int(input())
    nums.append(a)
nums.sort()
for i in nums:
    print(i)