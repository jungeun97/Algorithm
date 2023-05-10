from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list((map(int, input().split()))))
    arr = deque(list(range(n)))

    i = 0
    while queue:
        if queue[0] == max(queue):
            i += 1
            queue.popleft()
            if arr.popleft() == m:
                print(i)

        elif queue[0] != max(queue):
            k = queue.popleft()
            queue.append(k)
            l = arr.popleft()
            arr.append(l)