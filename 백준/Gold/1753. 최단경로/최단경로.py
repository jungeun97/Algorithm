import heapq
import sys


def dijkstra(s):
    dist[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))

    while heap:
        dis, now = heapq.heappop(heap)
        # if dist[now] < dis:
        #     continue
        for i in graph[now]:
            cost = dis + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
INF = sys.maxsize
dist = [INF] * (v+1)
visited = [0] * (v+1)
k = int(input())
for _ in range(e):
    u, x, w = map(int, input().split())
    graph[u].append((x, w))

dijkstra(k)

for i in range(1, v+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
