# https://www.acmicpc.net/problem/1541
from sys import stdin

# '-' 를 기준으로 분리
s = list(stdin.readline().split('-'))

# 첫 '-' 가 나올 때 까지의 숫자 합 만큼에서 나머지를 모두 빼면 됨
total = sum(map(int, s[0].split('+')))
for i in range(1, len(s)):
    total -= sum(map(int, s[i].split('+')))

print(total)
