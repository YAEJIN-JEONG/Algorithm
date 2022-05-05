# https://www.acmicpc.net/problem/1005
# ACM Craft
# 위상 정렬
from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    n, k = map(int, stdin.readline().split())

    time = [0]
    time.extend(list(map(int, stdin.readline().split())))
    # 진출 노드
    out_nodes = [[] for _ in range(n + 1)]
    # 진입 차수
    in_count = [0 for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        out_nodes[x].append(y)
        in_count[y] += 1

    w = int(stdin.readline())
    # min_time[i] 는 i 건물을 짓기 위해 필요한 최소 시간
    min_time = [0 for _ in range(n + 1)]
    answer = 0

    # 진입 차수가 0인 모든 노드 큐에 입력
    deq = deque()
    for i in range(1, n + 1):
        if in_count[i] == 0:
            deq.append(i)

    # 목표하는 건물의 진입 차수가 0이 될 때 까지
    while in_count[w] > 0:
        now = deq.popleft()

        for nxt in out_nodes[now]:
            # 최소 시간 갱신
            min_time[nxt] = max(min_time[nxt], min_time[now] + time[now])
            in_count[nxt] -= 1
            # 현재 처리중인 노드 nxt 의 진입 차수가 0이 되면 큐에 입력
            if in_count[nxt] == 0:
                deq.append(nxt)

    print(min_time[w] + time[w])
