# https://www.acmicpc.net/problem/2407
# 조합
from sys import stdin

n, m = map(int, stdin.readline().split())

answer = 1
for i in range(n, n - m, -1):
    answer *= i
for i in range(m, 0, -1):
    answer //= i

print(answer)
