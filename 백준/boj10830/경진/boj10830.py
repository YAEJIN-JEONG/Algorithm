# https://www.acmicpc.net/problem/10830
# 행렬 제곱
from sys import stdin


def divide_and_conquer(k):
    global matrix
    # 1 제곱이면 입력 행렬 그대로 반환
    if k == 1:
        return matrix

    # 행렬의 sqrt 구함
    matrix_sqrt = divide_and_conquer(k // 2)
    # 구한 sqrt 를 제곱
    result = matrix_multiply(matrix_sqrt, matrix_sqrt)

    # k가 짝수이면 그대로
    if k % 2 == 0:
        return result
    # k가 홀수이면 sqrt 구할 때 1이 버려졌으므로 한 번 곱해줌
    else:
        return matrix_multiply(result, matrix)


# 행렬 m1, m2 를 곱한 결과 반환
def matrix_multiply(m1, m2):
    size = len(m1)
    r = [[0 for _ in range(size)] for _ in range(size)]

    for x in range(size):
        for y in range(size):
            total = 0
            for i in range(size):
                total += m1[x][i] * m2[i][y]
            r[x][y] = total % 1000

    return r


if __name__ == '__main__':
    n, b = map(int, stdin.readline().split())
    # 원소는 1000으로 나눈 나머지. 1000이 입력될 수도 있음. 미리 처리하기.
    matrix = [[i % 1000 for i in (map(int, stdin.readline().split()))] for _ in range(n)]

    # 분할 정복
    result_matrix = divide_and_conquer(b)

    for elem in result_matrix:
        print(*elem)
