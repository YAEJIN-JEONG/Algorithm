# https://www.acmicpc.net/problem/11279
# 최대 힙
from sys import stdin
import heapq

n = int(stdin.readline())

q = []
for _ in range(n):
    x = int(stdin.readline())
    # heapq 는 최소 힙 이므로 (-) 부호를 사용해 최대 힙으로 사용
    if x == 0:
        print(-heapq.heappop(q) if q else 0)
    else:
        heapq.heappush(q, -x)
