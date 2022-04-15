# https://www.acmicpc.net/problem/2667
from sys import stdin
from collections import deque

n = int(stdin.readline())

array = []
for _ in range(n):
    array.append(stdin.readline())

deq = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
# 단지 크기 저장
count = []

for x in range(n):
    for y in range(n):
        if array[x][y] == '1' and not visited[x][y]:
            # bfs
            deq.append((x, y))
            visited[x][y] = True
            cnt = 1

            while deq:
                cx, cy = deq.popleft()

                steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for step in steps:
                    nx = cx + step[0]
                    ny = cy + step[1]

                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and array[nx][ny] == '1':
                        deq.append((nx, ny))
                        visited[nx][ny] = True
                        cnt += 1
            # 단지 크기 추가
            count.append(cnt)

count.sort()
# 단지 개수
print(len(count))
# 단지 크기 오름차순
print('\n'.join(map(str, count)))
