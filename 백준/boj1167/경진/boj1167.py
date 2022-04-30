# https://www.acmicpc.net/problem/1167
# 트리의 지름
from sys import stdin
from collections import deque


def bfs(v):
    global n, ad_list
    # 가장 먼 거리에 위치한 노드 (번호, 거리)
    max_dist = (v, 0)
    deq = deque()
    deq.append((v, 0))
    visited = [False] * (n + 1)
    visited[v] = True

    while deq:
        x, cost = deq.popleft()

        if max_dist[1] < cost:
            max_dist = (x, cost)

        for k, c in ad_list[x].items():
            if not visited[k]:
                visited[k] = True
                deq.append((k, cost + c))

    return max_dist


if __name__ == '__main__':
    n = int(stdin.readline())
    # 인접 리스트. index 가 노드 번호. {연결된 노드: 거리}
    ad_list = [{} for _ in range(n + 1)]

    for _ in range(n):
        s = list(map(int, stdin.readline().split()[:-1]))
        for j in range(1, len(s), 2):
            ad_list[s[0]][s[j]] = s[j + 1]

    # 임의의 노드 v 에서 가장 먼 노드 v1 을 찾음
    v1 = bfs(1)[0]
    # v1 에서 가장 먼 노드 까지의 거리가 트리의 지름
    answer = bfs(v1)[1]

    print(answer)
