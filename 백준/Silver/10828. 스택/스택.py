import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    word = sys.stdin.readline().split()
    a = word[0]
    if a == 'push':
        nums.append(word[1])
    elif a == 'pop':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums.pop())
    elif a == 'size':
        print(len(nums))
    elif a == 'empty':
        if len(nums) == 0:
            print(1)
        else:
            print(0)
    elif a == 'top':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[-1])