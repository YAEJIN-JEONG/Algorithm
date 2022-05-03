# https://www.acmicpc.net/problem/1238
# 파티
from sys import stdin
import heapq


# 다익스트라 (한 정점에서 다른 모든 정점까지 최단거리)
def dijkstra(start):
    global n, ad_list

    inf = 1000000000
    # 거리 배열 초기화
    distance = [inf] * (n + 1)
    distance[start] = 0

    # 시작점 우선순위 큐에 입력
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, now = heapq.heappop(q)
        # 처리 여부 확인 (방문 여부 대신 사용)
        if distance[now] >= cost:
            # start -> now -> ad[0]
            for ad in ad_list[now]:
                # start -> ad[0] 보다
                # start -> now -> ad[0] 이 더 짧으면 갱신하고 큐에 입력
                if distance[ad[0]] > cost + ad[1]:
                    distance[ad[0]] = cost + ad[1]
                    heapq.heappush(q, (cost + ad[1], ad[0]))

    return distance


if __name__ == '__main__':
    n, m, x = map(int, stdin.readline().split())

    # 인접 리스트. index 가 노드 번호. (연결된 노드, 거리)
    ad_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        v, i, j = map(int, stdin.readline().split())
        ad_list[v].append((i, j))

    # n -> x 로 가는 최단 거리
    cost_sum = [0]
    for i in range(1, n + 1):
        cost_sum.append(dijkstra(i)[x])

    # n -> x 로 가는 최단 거리에서 x -> n 으로 가는 최단 거리 더하기
    x2n = dijkstra(x)
    for i in range(1, n + 1):
        cost_sum[i] += x2n[i]

    print(max(cost_sum))
