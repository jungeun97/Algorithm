from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    word = sys.stdin.readline().split()
    a = word[0]
    if a == 'push_back':
        q.append(word[1])
    elif a == 'push_front':
        q.appendleft(word[1])
    elif a == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif a == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif a == 'size':
        print(len(q))
    elif a == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif a == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q) - 1])
