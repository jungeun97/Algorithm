import sys; input = sys.stdin.readline

def dfs(day, hap):
    global maxV
    if day == n:
        maxV = max(maxV, hap)
        return
    time = timeline[day][0]
    money = timeline[day][1]

    if day + time <= n:
        dfs(day + time, hap + money)
    dfs(day+1, hap)

n = int(input())
timeline = []
for i in range(n):
    t, p = map(int, input().split())
    timeline.append((t, p))

# print(timeline)
maxV = 0
for i in range(0, n):
    dfs(i, 0)
print(maxV)