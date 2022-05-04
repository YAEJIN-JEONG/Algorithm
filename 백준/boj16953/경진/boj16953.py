# https://www.acmicpc.net/problem/16953
# A → B
# bfs 로 풀었음
# 다른 풀이: B → A 를 한다고 생각하고 맨 뒤에 1 있으면 1제거, 2로 나누어지면 2로 나누기
from sys import stdin
from collections import deque

a, b = map(int, stdin.readline().split())

# 방문한 숫자: 카운트
visited = {}
deq = deque()
deq.append(a)
visited[a] = 0

# bfs
while deq:
    now = deq.popleft()

    if now == b:
        print(visited[now] + 1)
        break
    elif now > b:
        continue
    else:
        for i in (now * 2, now * 10 + 1):
            if i not in visited:
                deq.append(i)
                visited[i] = visited[now] + 1
else:
    print(-1)
