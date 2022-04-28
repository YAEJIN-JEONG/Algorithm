# https://www.acmicpc.net/problem/1753
# 최단경로
from sys import stdin
import heapq


# 다익스트라 (한 정점에서 다른 모든 정점 까지 최단 거리)
def dijkstra(start):
    global v, ad_list, inf

    distance = [inf] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] >= cost:
            for n, w in ad_list[now]:
                new_cost = distance[now] + w
                if distance[n] > new_cost:
                    distance[n] = new_cost
                    heapq.heappush(q, (new_cost, n))

    return distance


if __name__ == '__main__':
    v, e = map(int, stdin.readline().split())
    k = int(stdin.readline())

    ad_list = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, stdin.readline().split())
        ad_list[a].append((b, c))

    inf = 1000000000
    dist = dijkstra(k)
    for i in range(1, len(dist)):
        print(dist[i] if dist[i] < inf else 'INF')
