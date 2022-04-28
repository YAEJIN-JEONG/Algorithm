# https://www.acmicpc.net/problem/17626
# Four Squares
from sys import stdin
import math

n = int(stdin.readline())

# n 보다 작거나 같은 모든 제곱수
squared = {i ** 2 for i in range(1, int(math.sqrt(n)) + 1)}

# n 이 제곱수 인 경우
if n in squared:
    print(1)
    exit()

# (n - 제곱수) 가 제곱수 인 경우
for i in range(1, int(math.sqrt(n)) + 1):
    if n - i ** 2 in squared:
        print(2)
        exit()

# (n - 제곱수 - 제곱수) 가 제곱수 인 경우
for i in range(1, int(math.sqrt(n)) + 1):
    k = n - i ** 2
    for j in range(1, int(math.sqrt(k)) + 1):
        if k - j ** 2 in squared:
            print(3)
            exit()

# 나머지
print(4)
