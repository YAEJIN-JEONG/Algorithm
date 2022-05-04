# https://www.acmicpc.net/problem/17070
# 파이프 옮기기 1
# PyPy3 로도 시간초과. 파이썬 이라서 그런듯.
# backtrack 내에서 반복문 대신 전부 if 문으로 바꾸면 되긴함.
# 그냥 자바로 다시 풀었음.
from sys import stdin


def backtrack(pipe):
    global n, answer, arr

    x, y, d = pipe

    if x == n - 1 and y == n - 1:
        answer += 1
    else:
        # 가로, 세로, 대각선 이동
        steps = [(0, 1), (1, 0), (1, 1)]

        for i in range(len(steps)):
            # 방향에 따라 이동할 수 없는 방향 스킵
            if (d == 0 and i == 1) or (d == 1 and i == 0):
                continue
            nx = x + steps[i][0]
            ny = y + steps[i][1]
            nd = i
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                # 대각선 방향인 경우 벽 추가 확인
                if i == 2 and (arr[nx - 1][ny] != 0 or arr[nx][ny - 1] != 0):
                    continue
                backtrack([nx, ny, nd])


if __name__ == '__main__':
    n = int(stdin.readline())

    arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

    # [행, 열, 방향]
    # 0: 가로, 1: 세로, 2: 대각선
    start = [0, 1, 0]
    answer = 0

    backtrack(start)

    print(answer)
