# https://www.acmicpc.net/problem/11286
from sys import stdin
import heapq

n = int(stdin.readline())

q = []
for _ in range(n):
    x = int(stdin.readline())

    # 최소 힙에 (key, value) 튜플로 넣음
    # key 기준 정렬, key 에 절댓값, 출력할 때는 value 출력
    if x == 0:
        print(0 if not q else heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(x), x))
