# https://www.acmicpc.net/problem/15650
# N과 M (2)
from sys import stdin
import itertools

n, m = map(int, stdin.readline().split())

nums = [i for i in range(1, n + 1)]

# nums 에서 m개 고르는 조합
combs = itertools.combinations(nums, m)

for comb in combs:
    print(*comb)
