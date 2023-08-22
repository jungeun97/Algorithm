a, b = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))
nums.reverse()

ten = 0
for i in range(m):
    ten += nums[i]*(a**i)

ans = []
while ten // b:
    ans.append(ten%b)
    ten //= b
ans.append(ten)

ans.reverse()
print(*ans)