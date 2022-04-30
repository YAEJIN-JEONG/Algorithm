# https://www.acmicpc.net/problem/2638
# 치즈
from sys import stdin
from collections import deque


def bfs():
    global n, m, cheese, deq, visited

    # 이번에 녹는 치즈
    melt = set()

    while deq:
        x, y = deq.popleft()

        steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if 0 <= nx < n and 0 <= ny < m:
                visited[nx][ny] += 1
                # 아직 방문하지 않은 빈 공간
                if cheese[nx][ny] == 0 and visited[nx][ny] == 1:
                    deq.append((nx, ny))
                # 2변 이상 접촉한 치즈
                elif cheese[nx][ny] == 1 and visited[nx][ny] >= 2:
                    melt.add((nx, ny))

    # 치즈 녹이기, 방문한 빈 공간으로 바꾸기
    for x, y in melt:
        cheese[x][y] = 0
        visited[x][y] = 1

    # 녹인 치즈 위치가 들어있는 큐 반환
    return deque(melt)


if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())

    cheese = [list(map(int, stdin.readline().split())) for _ in range(n)]

    # 초기 세팅, 가장자리에는 치즈가 없으므로 (0, 0) 에서 탐색 시작
    deq = deque()
    visited = [[0] * m for _ in range(n)]
    deq.append((0, 0))
    visited[0][0] = 1

    answer = -1

    while deq:
        # 치즈를 녹이고, 녹인 치즈의 위치가 담긴 큐로 교체
        deq = bfs()
        answer += 1

    print(answer)
