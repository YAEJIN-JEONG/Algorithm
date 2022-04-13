# https://www.acmicpc.net/problem/1780
from sys import stdin


def divide(array, x, y, size):
    global count
    # 모두 같은 수로 되어 있으면 카운트 후 종료
    if match(array, x, y, size):
        count[array[x][y] + 1] += 1
        return

    # 종이 9분할로 자르기 (재귀)
    size //= 3
    for i in range(0, 3):
        for j in range(0, 3):
            divide(array, x + i * size, y + j * size, size)


def match(array, x, y, size):
    # 모두 같은 수로 되어 있는지 반환
    k = array[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if array[i][j] != k:
                return False
    return True


if __name__ == '__main__':
    n = int(stdin.readline())
    arr, count = [], [0, 0, 0]

    for _ in range(n):
        arr.append(list(map(int, stdin.readline().split())))

    # 종이 자르고 세기
    divide(arr, 0, 0, n)
    # 정답 출력
    print('\n'.join(map(str, count)))
