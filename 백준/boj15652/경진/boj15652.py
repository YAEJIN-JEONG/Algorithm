# https://www.acmicpc.net/problem/15652
# N과 M (4)
from sys import stdin
import itertools

n, m = map(int, stdin.readline().split())

nums = [i for i in range(1, n + 1)]

# 중복 조합 구하기
combs = itertools.combinations_with_replacement(nums, m)

for comb in combs:
    print(*comb)
