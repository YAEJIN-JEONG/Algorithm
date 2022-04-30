# https://www.acmicpc.net/problem/2448
# 별 찍기 - 11
from sys import stdin


def rec(x, y, k):
    global triangle

    if k == 3:
        # 첫번째, 두번째, 세번째 줄
        triangle[x][y] = '*'
        triangle[x + 1][y - 1] = triangle[x + 1][y + 1] = '*'
        for i in range(3):
            triangle[x + 2][y - i] = '*'
            triangle[x + 2][y + i] = '*'
    else:
        k //= 2
        # 가운데, 왼쪽, 오른쪽 삼각형
        rec(x, y, k)
        rec(x + k, y - k, k)
        rec(x + k, y + k, k)


if __name__ == '__main__':
    n = int(stdin.readline())

    triangle = [[' ' for _ in range(2 * n)] for _ in range(n)]

    # 재귀
    rec(0, n - 1, n)

    for line in triangle:
        print(''.join(line))
