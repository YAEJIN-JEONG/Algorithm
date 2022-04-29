# https://www.acmicpc.net/problem/1916
# 최소비용 구하기
from sys import stdin
import heapq


# 다익스트라
def dijkstra(start):
    global n, ad_list

    inf = 1000000000
    distance = [inf] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for v, w in ad_list[now]:
            new_cost = cost + w
            if distance[v] > new_cost:
                distance[v] = new_cost
                heapq.heappush(q, (new_cost, v))

    return distance


if __name__ == '__main__':
    n = int(stdin.readline())
    m = int(stdin.readline())

    ad_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        ad_list[a].append((b, c))

    s, e = map(int, stdin.readline().split())

    s_dist = dijkstra(s)
    print(s_dist[e])
