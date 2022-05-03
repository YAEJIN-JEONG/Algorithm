# https://acmicpc.net/problem/11779
# 최소비용 구하기 2
from sys import stdin
import heapq


# 다익스트라 (경로 포함)
def dijkstra(start):
    global n, edges
    inf = 1000000000
    # 직전에 어디를 거쳐왔는지 저장
    parents = [0] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    cost = [inf] * (n + 1)
    cost[start] = 0
    parents[start] = start

    while q:
        cost_now, now = heapq.heappop(q)

        if cost[now] < cost_now:
            continue

        for v, w in edges[now]:
            new_cost = cost_now + w
            if new_cost < cost[v]:
                cost[v] = new_cost
                heapq.heappush(q, (new_cost, v))
                parents[v] = now

    return cost, parents


# 직전에 겨처온 경로들을 거슬러 올라가서 경로 알아내기
def rec(parents, child):
    if parents[child] == child:
        return [child]
    else:
        li = rec(parents, parents[child])
        li.append(child)
        return li


if __name__ == '__main__':
    n = int(stdin.readline())
    m = int(stdin.readline())

    edges = [[] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        edges[a].append((b, c))

    s, e = map(int, stdin.readline().split())

    # 시작점 s로 하는 다익스트라 결과 배열, 경로 추적할 배열
    cost, parents = dijkstra(s)

    # e 까지 가는 경로 알아내기
    path = rec(parents, e)
    print(cost[e])
    print(len(path))
    print(' '.join(map(str, path)))
