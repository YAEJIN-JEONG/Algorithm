# https://www.acmicpc.net/problem/17144
# 미세먼지 안녕!
from sys import stdin
from collections import deque


def spread():
    global r, c, room, steps
    
    # 먼지 위치 큐에 넣기
    deq = deque()
    for x in range(r):
        for y in range(c):
            if room[x][y] > 0:
                deq.append((x, y, room[x][y]))

    # 먼지 확산
    while deq:
        x, y, amount = deq.popleft()

        # 먼지 양이 5보다 작으면 확산 안됨
        if amount < 5:
            continue

        # 확산된 방향 수
        count = 0
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                room[nx][ny] += amount // 5
                count += 1

        room[x][y] -= amount // 5 * count


def circulation(x, y, order):
    global r, c, room, cleaner, steps
    prev = 0

    for o in order:
        while True:
            nx = x + steps[o][0]
            ny = y + steps[o][1]

            if 0 <= nx < r and 0 <= ny < c:
                room[x][y], prev = prev, room[x][y]
                x, y = nx, ny
                # 공기 청정기 만나면 종료
                if room[nx][ny] == -1:
                    break
            else:
                # 이동가능한 범위를 벗어나면 다음 방향으로 진행
                break


if __name__ == '__main__':
    r, c, t = map(int, stdin.readline().split())

    room = [[0] * c for _ in range(r)]
    # 공기 청정기 위치 [위쪽, 아래쪽]
    cleaner = []
    for i in range(r):
        s = list(map(int, stdin.readline().split()))
        for j in range(c):
            room[i][j] = s[j]
            if s[j] == -1:
                cleaner.append((i, j))

    steps = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    for _ in range(t):
        # 먼지 확산
        spread()
        # 공기 청정기 윗쪽 순환 (순환 시작 위치, 순환 방향 순서. steps 기준)
        circulation(cleaner[0][0], cleaner[0][1] + 1, [0, 1, 2, 3])
        # 공기 청정기 아래쪽 순환
        circulation(cleaner[1][0], cleaner[1][1] + 1, [0, 3, 2, 1])

    print(sum(map(sum, room)) + 2)
