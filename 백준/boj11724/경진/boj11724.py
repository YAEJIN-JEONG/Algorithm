# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
# 인접 리스트
ad_list = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 인접 리스트 입력
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    ad_list[u].append(v)
    ad_list[v].append(u)

# 연결 요소 개수
answer = 0

deq = deque()
for i in range(1, n + 1):
    # i 가 아직 방문되지 않은 정점이면 연결 요소 + 1
    if not visited[i]:
        answer += 1
        deq.append(i)
        visited[i] = True

        # i 를 통해 갈 수 있는 모든 정점 방문
        while deq:
            v = deq.popleft()
            for j in ad_list[v]:
                if not visited[j]:
                    deq.append(j)
                    visited[j] = True

print(answer)
