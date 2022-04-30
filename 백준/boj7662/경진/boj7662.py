# https://www.acmicpc.net/problem/7662
# 이중 우선순위 큐
from sys import stdin
import heapq

t = int(stdin.readline())

for _ in range(t):
    k = int(stdin.readline())
    # 삭제된 원소 인지 (index -> 힙에 입력된 순서)
    deleted = [False for _ in range(k)]
    # 최소 힙, 최대 힙
    min_heap, max_heap = [], []

    for i in range(k):
        c, n = stdin.readline().split()

        if c == 'D':
            # 현재 처리 할 힙 결정
            current_heap = min_heap if n == '-1' else max_heap
            # 힙에서 꺼낸 원소가 삭제되지 않은 원소일 때만 처리 (삭제된 원소 버림)
            while current_heap and deleted[current_heap[0][1]]:
                heapq.heappop(current_heap)
            # 삭제되지 않은 원소 이면 꺼내서 삭제 체크 후, 버림
            if current_heap:
                deleted[heapq.heappop(current_heap)[1]] = True
        else:
            heapq.heappush(min_heap, (int(n), i))
            heapq.heappush(max_heap, (-int(n), i))

    # 마지막으로 최소, 최대 힙 동기화 (삭제된 원소 다 버리기)
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # 정답 출력
    if min_heap and max_heap:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
    else:
        print('EMPTY')
