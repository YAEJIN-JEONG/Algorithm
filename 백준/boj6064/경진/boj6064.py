# https://www.acmicpc.net/problem/6064
# 카잉 달력
from sys import stdin
import math

t = int(stdin.readline())

for _ in range(t):
    m, n, x, y = map(int, stdin.readline().split())
    # 마지막 해는 m, n의 최소 공배수
    lcm = m * n // math.gcd(m, n)
    # 년도를 m씩 증가, x는 고정 y 값만 바꿈
    # y 는 m씩 더하고 n 으로 나눈 나머지 값. (나머지 0 이면 n 이므로 y-1 의 나머지에 +1 해줌)
    cnt = x
    ny = (x - 1) % n + 1
    while True:
        if cnt > lcm:
            cnt = -1
            break
        if ny == y:
            break
        cnt += m
        ny = (ny + m - 1) % n + 1

    print(cnt)
