n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()
a = sum(nums) / n

print(round(a))

print(nums[n//2])

dict = {}
for i in range(n):
    if nums[i] in dict.keys():
        dict[nums[i]] += 1
    else:
        dict[nums[i]] = 1
maxV = max(dict.values())
maxL = []

for i in dict:
    if maxV == dict[i]:
        maxL.append(i)

if len(maxL) > 1:
    print(maxL[1])
else:
    print(maxL[0])

print(nums[-1] - nums[0])