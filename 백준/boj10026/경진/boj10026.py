# https://www.acmicpc.net/problem/10026
# 적록색약
from sys import stdin
from collections import deque


def bfs(picture, x, y, i):
    # i 가 0이면 적록색약 아닌 거, 1이면 적록색약
    global cnt, visited
    color = picture[i][x][y]
    cnt[i] += 1

    deq = deque()
    deq.append((x, y))
    visited[i][x][y] = True

    while deq:
        cx, cy = deq.popleft()

        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for step in steps:
            nx = cx + step[0]
            ny = cy + step[1]

            if 0 <= nx < len(picture[i]) and 0 <= ny < len(picture[i]) and not visited[i][nx][ny] and picture[i][nx][ny] == color:
                deq.append((nx, ny))
                visited[i][nx][ny] = True


if __name__ == '__main__':
    n = int(stdin.readline())

    # 적록색약 아닌 사람 시점, 적록색약 시점 으로 나눔
    picture = [[], []]

    for _ in range(n):
        s = stdin.readline().rstrip()
        picture[0].append(s)
        picture[1].append(s.replace('G', 'R'))

    # 0번 인덱스 적록색약x, 1번 인덱스 적록색약o
    cnt = [0, 0]
    visited = [[[False for _ in range(n)] for _ in range(n)], [[False for _ in range(n)] for _ in range(n)]]

    # 각각 bfs
    for x in range(n):
        for y in range(n):
            if not visited[0][x][y]:
                bfs(picture, x, y, 0)
            if not visited[1][x][y]:
                bfs(picture, x, y, 1)

    # 정답 출력
    print(cnt[0], cnt[1])
