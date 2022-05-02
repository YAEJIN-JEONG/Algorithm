# https://www.acmicpc.net/problem/11444
# 피보나치 수 6
from sys import stdin


def divide_and_conquer(k):
    global fibo

    # 이미 계산된 값인 경우
    if k in fibo:
        return fibo[k]
    else:
        if k % 2 == 1:
            result = (divide_and_conquer(k // 2) ** 2 + divide_and_conquer(k // 2 + 1) ** 2) % 1000000007
        else:
            result = (divide_and_conquer(k + 1) - divide_and_conquer(k - 1)) % 1000000007

        fibo[k] = result
        return fibo[k]


if __name__ == '__main__':
    n = int(stdin.readline())
    # 이미 계산된 값 저장.
    fibo = {0: 0, 1: 1, 2: 1}
    # 규칙
    # n 이 홀수 -> f(n) = f(n // 2)^2 + f(n // 2 + 1)^2
    # n 이 짝수 -> f(n) = f(n + 1) - f(n - 1)
    print(divide_and_conquer(n))
