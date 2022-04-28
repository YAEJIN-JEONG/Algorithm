# https://www.acmicpc.net/problem/1043
# 거짓말
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

# 진실을 아는 사람들
know_truth = {i for i in stdin.readline()[1:].rstrip().split()}
# 파티 리스트
party_list = [set(stdin.readline()[1:].rstrip().split()) for _ in range(m)]

# bfs (진실을 아는 사람들 확장)
deq = deque()
visited = [False] * len(party_list)

# 진실을 아는 사람들이 포함된 파티 찾아서 큐에 입력
for i, party in enumerate(party_list):
    for elem in know_truth:
        if elem in party:
            deq.append(i)
            visited[i] = True
            know_truth |= party
            break

# 큐에 입력되어 있는 파티를 통해 도달할 수 있는 모든 파티 탐색
while deq:
    k = deq.popleft()

    for i in party_list[k]:
        for j in range(len(party_list)):
            if not visited[j] and i in party_list[j]:
                deq.append(j)
                visited[j] = True
                know_truth |= party_list[j]

# 진실을 아는 사람이 없는 파티 개수
answer = 0
for party in party_list:
    if len(party & know_truth) == 0:
        answer += 1

print(answer)
