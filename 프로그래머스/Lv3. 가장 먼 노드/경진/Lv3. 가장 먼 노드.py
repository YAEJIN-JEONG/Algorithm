# https://programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque


# bfs 하면서 거리 저장
# 그래프 인접행렬로 표현했는데 시간초과. 인접리스트로 변경
def solution(n, edge):
    # 방문 겸 거리 저장 리스트
    distance = [-1] * (n + 1)
    ad_list = [[] for _ in range(n + 1)]

    # 인접 리스트 만들기, 인덱스가 노드 번호
    for a, b in edge:
        ad_list[a].append(b)
        ad_list[b].append(a)

    # bfs
    dq = deque()
    dq.append(1)
    distance[1] = 0

    while dq:
        v = dq.popleft()
        # 방문하지 않은 인접 노드 처리 후, 큐에 추가
        for i in ad_list[v]:
            if distance[i] == -1:
                distance[i] = distance[v] + 1
                dq.append(i)

    return distance.count(max(distance))
