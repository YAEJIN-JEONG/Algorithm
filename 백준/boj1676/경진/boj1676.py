# https://www.acmicpc.net/problem/1676
from sys import stdin

n = int(stdin.readline())
# 소인수 분해하여 (2x5) 의 지수 만큼 0이 생김
# 소인수 분해결과는 항상 5보다 2의 개수가 많으므로 5 결과만 세기
five_count = 0

for i in range(5, n + 1):
    while i > 1 and i % 5 == 0:
        five_count += 1
        i //= 5

print(five_count)
