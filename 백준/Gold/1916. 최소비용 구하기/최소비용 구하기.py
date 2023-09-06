import heapq
import sys


def dijkstra(v):
    visited[v] = 1
    heap = []
    heapq.heappush(heap, (0, v))
    while heap:
        dis, now = heapq.heappop(heap)
        if dist[now] < dis:
            continue
        for i in graph[now]:
            cost = dis + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))



n = int(input())
m = int(input())
INF = sys.maxsize
graph = [[] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
dist = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, e = map(int, input().split())
dijkstra(s)
print(dist[e])