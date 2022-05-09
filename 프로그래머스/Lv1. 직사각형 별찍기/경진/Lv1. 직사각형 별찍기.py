# https://programmers.co.kr/learn/courses/30/lessons/12969
from sys import stdin

n, m = map(int, stdin.readline().split())

for _ in range(m):
    print('*' * n)
