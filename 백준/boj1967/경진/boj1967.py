# https://www.acmicpc.net/problem/1967
# 트리의 지름
from sys import stdin
from collections import deque


def bfs(start):
    global n, edges
    # 가장 멀리 있는 노드 (거리, 노드번호) 반환
    max_value = (0, start)
    visited = [False] * (n + 1)
    deq = deque()
    deq.append((0, start))
    visited[start] = True

    while deq:
        cost, v = deq.popleft()

        if cost > max_value[0]:
            max_value = (cost, v)

        for to, w in edges[v]:
            if not visited[to]:
                deq.append((cost + w, to))
                visited[to] = True

    return max_value


if __name__ == '__main__':
    n = int(stdin.readline())

    edges = [[] for _ in range(n + 1)]

    while True:
        s = stdin.readline().rstrip()
        if len(s) == 0:
            break

        a, b, c = map(int, s.split())
        edges[a].append((b, c))
        edges[b].append((a, c))

    # 트리의 지름은 임의의 노드에서 가장 멀리 있는 v1 을 찾으면
    # v1 에서 다시 가장 멀리 있는 노드까지의 거리가 지름
    v1 = bfs(1)[1]
    print(bfs(v1)[0])
