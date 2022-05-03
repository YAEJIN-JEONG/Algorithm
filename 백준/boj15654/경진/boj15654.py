# https://www.acmicpc.net/problem/15654
# N과 M (5)
from sys import stdin
import itertools

n, m = map(int, stdin.readline().split())

nums = sorted(list(map(int, stdin.readline().split())))

# 순열 구하기
permutes = itertools.permutations(nums, m)

for p in permutes:
    print(*p)
