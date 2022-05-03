# https://www.acmicpc.net/problem/14502
# 연구소
from sys import stdin
from collections import deque
import itertools
import copy


def bfs():
    global n, m, arr, virus

    deq = deque(virus)
    # 이차원리스트 그냥 copy() 하면 원본 참조되버림. copy 모듈에서 deepcopy() 쓰거나
    # row 마다 copy() 또는 슬라이싱 복사([:]) 해야됨
    n_arr = copy.deepcopy(arr)

    # 전염시키기
    while deq:
        x, y = deq.popleft()

        steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if 0 <= nx < n and 0 <= ny < m and n_arr[nx][ny] == 0:
                deq.append((nx, ny))
                n_arr[nx][ny] = 2

    # 안전영역 넓이
    area = 0
    for row in n_arr:
        area += row.count(0)

    return area


if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())

    arr = [[0] * m for _ in range(n)]
    # 빈 공간, 바이러스 위치
    space, virus = [], []
    for i in range(n):
        s = list(map(int, stdin.readline().split()))

        for j in range(m):
            arr[i][j] = s[j]
            if s[j] == 0:
                space.append((i, j))
            elif s[j] == 2:
                virus.append((i, j))

    # 빈 공간 세 개 고르는 조합 (벽 세우기)
    comb = itertools.combinations(space, 3)

    answer = 0
    for (x1, y1), (x2, y2), (x3, y3) in comb:
        arr[x1][y1] = arr[x2][y2] = arr[x3][y3] = 1
        answer = max(answer, bfs())
        arr[x1][y1] = arr[x2][y2] = arr[x3][y3] = 0

    print(answer)
