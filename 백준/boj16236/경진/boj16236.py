# https://www.acmicpc.net/problem/16236
# 아기 상어
from sys import stdin
from collections import deque


# 물고기 먹기
# 시간 증가, 먹은 물고기 위치 0 만들기, 상어 위치 바꾸기, 경험치 증가 및 레벨업
def eat(d, x, y):
    global space, pos, time, exp, level
    time += d
    space[x][y] = 0
    pos = (0, x, y)
    exp += 1
    if exp >= level:
        level += 1
        exp = 0


def bfs():
    global n, space, pos

    visited = [[False for _ in range(n)] for _ in range(n)]
    # 이동할 수 있는 모든 곳 저장 (거리, x, y)
    move_list = []
    deq = deque()
    deq.append(pos)
    visited[pos[1]][pos[2]] = True

    while deq:
        d, x, y = deq.popleft()

        steps = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for step in steps:
            nx, ny = x + step[0], y + step[1]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and space[nx][ny] <= level:
                deq.append((d + 1, nx, ny))
                move_list.append((d + 1, nx, ny))
                visited[nx][ny] = True

    # 정렬 (거리가 가깝고 x, y 좌표가 더 작은 순서대로)
    move_list.sort()
    for move in move_list:
        d, x, y = move
        # 먹을 수 있는 물고기면 먹고 종료
        if 0 < space[x][y] < level:
            eat(d, x, y)
            return True

    return False


if __name__ == '__main__':
    n = int(stdin.readline())
    space = [[i for i in map(int, stdin.readline().split())] for _ in range(n)]

    # 상어 크기, 경험치, 흐른 시간, 상어 위치 (거리, x, y)
    level, exp, time, pos = 2, 0, 0, (0, 0, 0)
    for r in range(n):
        for c in range(n):
            if space[r][c] == 9:
                pos = (0, r, c)
                space[r][c] = 0

    # 먹을 물고기 없을 때 까지
    while bfs():
        pass

    print(time)
