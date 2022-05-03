# https://www.acmicpc.net/problem/13549
# 숨바꼭질 3
from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())

# visited[i] 는 i 위치 까지 걸린 시간
visited = [-1 for _ in range(100001)]
deq = deque()
deq.append(n)
visited[n] = 0

while deq:
    now = deq.popleft()

    if now == k:
        break

    for pos in (now - 1, now + 1, now * 2):
        # 순간이동 할 땐 0초
        time = visited[now] + 1 if pos != now * 2 else visited[now]

        if 0 <= pos <= 100000:
            # 아직 방문하지 않은 경우
            if visited[pos] == -1:
                deq.append(pos)
                visited[pos] = time
            # 방문했던 곳인데 더 빨리 도착한 경우
            elif visited[pos] > time:
                visited[pos] = time

print(visited[k])
