# https://www.acmicpc.net/problem/2630
from sys import stdin


# 비슷한 문제 boj1780, boj1992
def divide(arr, x, y, size):
    global count
    if match(arr, x, y, size):
        count[int(arr[x][y])] += 1
    else:
        size //= 2

        for i in range(0, 2):
            for j in range(0, 2):
                divide(arr, x + size * i, y + size * j, size)


def match(arr, x, y, size):
    k = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != k:
                return False
    return True


if __name__ == '__main__':
    n = int(stdin.readline())

    array = []
    for _ in range(n):
        array.append(stdin.readline().split())

    count = [0, 0]
    divide(array, 0, 0, n)

    print('\n'.join(map(str, count)))
