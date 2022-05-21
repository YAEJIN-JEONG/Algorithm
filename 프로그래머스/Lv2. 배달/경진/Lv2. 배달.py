# https://programmers.co.kr/learn/courses/30/lessons/12978
import heapq
INF = 500001


def dijkstra(start, n, edges):
    distance, q = [INF] * (n + 1), []
    distance[start] = 0

    heapq.heappush(q, (0, start))

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for to, c in edges[now]:
            # start -> to 보다 start -> now -> to 가 빠르면 갱신
            new_cost = distance[now] + c

            if distance[to] > new_cost:
                distance[to] = new_cost
                heapq.heappush(q, (new_cost, to))

    return distance


def solution(n, road, k):
    edges = [[] for _ in range(n + 1)]
    for a, b, c in road:
        edges[a].append([b, c])
        edges[b].append([a, c])

    distance = dijkstra(1, n, edges)

    return len(list(filter(lambda x: x <= k, distance)))
