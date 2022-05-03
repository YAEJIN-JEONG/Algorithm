# https://www.acmicpc.net/problem/13172
# Σ
from sys import stdin
import math


# 거듭 제곱 분할-정복
def divide_and_conquer(x, k):
    global mod_n

    if k == 1:
        return x

    # 스퀘어 루트 구하기
    sqrt = divide_and_conquer(x, k // 2)

    # k 가 짝수이면 sqrt 그대로 제곱
    if k % 2 == 0:
        return (sqrt ** 2) % mod_n
    # 홀수이면 1이 버려졌으므로 x 한번 더 곱해주기
    else:
        return (sqrt ** 2) * x % mod_n


if __name__ == '__main__':
    m = int(stdin.readline())

    mod_n = 1000000007
    answer = 0
    for _ in range(m):
        n, s = map(int, stdin.readline().split())
        # 기약 분수로 만들기
        gcd = math.gcd(n, s)
        n //= gcd
        s //= gcd

        # n 의 mod-2 제곱 구하고 계산해서 정답에 더해주기
        answer += s * divide_and_conquer(n, mod_n - 2) % mod_n

    print(answer % mod_n)
