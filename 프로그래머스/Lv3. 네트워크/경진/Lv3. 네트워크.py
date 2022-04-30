# https://programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque


def solution(n, computers):
    deq = deque()
    visited = [False for _ in range(n)]
    answer = 0
    # 0 ~ n-1 번 컴퓨터 까지 탐색
    for i in range(n):
        # 아직 네트워크에 속하지 않은 컴퓨터인 경우
        if not visited[i]:
            answer += 1
            # bfs, 이 컴퓨터와 같은 네트워크에 연결된 모든 컴퓨터를 탐색
            deq.append(i)
            visited[i] = True

            while deq:
                v = deq.popleft()

                for j in range(n):
                    if computers[v][j] == 1 and not visited[j]:
                        deq.append(j)
                        visited[j] = True

    return answer
