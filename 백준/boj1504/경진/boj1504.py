# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로
from sys import stdin
import heapq


# 다익스트라 (start 에서 모든 노드까지의 최단 거리)
def dijkstra(start):
    global n, ad_list, inf

    # 거리 배열 초기화
    distance = [inf for _ in range(n + 1)]

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        # 방문 여부 확인
        if distance[now] <= cost:
            # start -> v 보다 start -> now -> v 가 더 짧으면 갱신하고 큐에 입력
            for v, d in ad_list[now].items():
                new_cost = cost + d
                if distance[v] > new_cost:
                    distance[v] = new_cost
                    heapq.heappush(q, (new_cost, v))

    return distance


if __name__ == '__main__':
    n, e = map(int, stdin.readline().split())

    ad_list = [{} for _ in range(n + 1)]
    for _ in range(e):
        a, b, c = map(int, stdin.readline().split())
        ad_list[a][b] = c
        ad_list[b][a] = c

    v1, v2 = map(int, stdin.readline().split())

    inf = 1000000000
    start_d = dijkstra(1)
    v1_d = dijkstra(v1)
    v2_d = dijkstra(v2)

    # start -> v1 -> v2 -> end
    # start -> v2 -> v1 -> end 중에 더 짧은 거리.
    answer = min(start_d[v1] + v1_d[v2] + v2_d[n], start_d[v2] + v2_d[v1] + v1_d[n])
    # answer 가 inf 보다 크거나 같으면 불가능
    answer = -1 if answer >= inf else answer

    print(answer)
