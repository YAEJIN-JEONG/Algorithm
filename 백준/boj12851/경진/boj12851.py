# https://www.acmicpc.net/problem/12851
# 숨바꼭질 2
from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())

# [걸린 시간, 경우의 수] 저장
visited = [[-1, 0] for _ in range(100001)]
deq = deque()
deq.append(n)
visited[n] = [0, 1]

while deq:
    now = deq.popleft()

    for pos in (now - 1, now + 1, now * 2):
        if 0 <= pos < 100001:
            # pos 까지 걸린 시간
            time = visited[now][0] + 1
            # pos 가 첫 방문이면 그 때가 최소 시간. pos 까지 온 경우의 수 저장
            if visited[pos][0] == -1:
                visited[pos][0] = time
                visited[pos][1] = visited[now][1]
                deq.append(pos)
            # pos 가 첫 방문이 아니지만 걸린 시간이 같다면 경우의 수 더해주기.
            elif visited[pos][0] == time:
                visited[pos][1] += visited[now][1]

print(visited[k][0])
print(visited[k][1])
