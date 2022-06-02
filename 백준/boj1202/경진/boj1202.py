# https://www.acmicpc.net/problem/1202
from sys import stdin
import heapq

n, k = map(int, stdin.readline().split())
# 보석, 가방 무게 기준 asc 정렬
jewelry = sorted([list(map(int, stdin.readline().split())) for _ in range(n)], key=lambda x: x[0])
capacities = sorted([int(stdin.readline()) for _ in range(k)])

answer, q, idx = 0, [], 0
for capacity in capacities:
    # 현재 가방 무게에 넣을 수 있는 보석 모두 heap 에 입력 (priority: 보석 가치)
    while idx < len(jewelry) and jewelry[idx][0] <= capacity:
        heapq.heappush(q, -jewelry[idx][1])
        idx += 1

    # 큐에 있는 가장 가치가 높은 보석 현재 가방에 담기
    if q:
        answer += -heapq.heappop(q)

print(answer)
