# https://www.acmicpc.net/problem/1629
# 곱셈
from sys import stdin


# x의 2n제곱 = x의 n제곱 의 제곱
def divide_and_conquer(x, y):
    global c
    # 1 제곱 인 경우 재귀 탈출
    if y == 1:
        return x % c

    # x 의 (y // 2) 제곱 구함
    sqrt = divide_and_conquer(x, y // 2)

    # y 가 짝수 이면 그대로 x 의 (y // 2) 을 제곱하면 됨
    # y 가 홀수 이면 나머지 1이 버려졌기 때문에 x 를 한번 더 곱함
    if y % 2 == 0:
        return sqrt * sqrt % c
    else:
        return sqrt * sqrt * a % c


if __name__ == '__main__':
    a, b, c = map(int, stdin.readline().split())
    print(divide_and_conquer(a, b))
