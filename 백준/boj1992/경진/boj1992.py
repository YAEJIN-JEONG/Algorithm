# https://www.acmicpc.net/problem/1992
from sys import stdin


# 영역 분할
def divide(array, x, y, size):
    # 현재 영역이 모두 같은 원소이면, 해당 원소 출력 후 종료
    if match(array, x, y, size):
        print(array[x][y], end='')
    else:
        # 4 영역으로 분할, 분할한 영역 각각을 재귀
        print('(', end='')
        size //= 2

        for i in range(0, 2):
            for j in range(0, 2):
                divide(array, x + size * i, y + size * j, size)
        print(')', end='')


# 영역 내 모두 같은 원소인지
def match(array, x, y, size):
    k = array[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if array[i][j] != k:
                return False
    return True


if __name__ == '__main__':
    n = int(stdin.readline())

    image = []

    for _ in range(n):
        image.append(list(stdin.readline()))

    # 4 영역으로 분할
    divide(image, 0, 0, n)
