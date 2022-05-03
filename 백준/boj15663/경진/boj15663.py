# https://www.acmicpc.net/problem/15663
# N과 M (9)
from sys import stdin
import itertools

n, m = map(int, stdin.readline().split())

nums = sorted(list(map(int, stdin.readline().split())))

# 순열 구하기
permutes = itertools.permutations(nums, m)

# 이미 출력된 순열 printed 에 저장
printed = set()
for p in permutes:
    if p not in printed:
        print(*p)
        printed.add(p)
