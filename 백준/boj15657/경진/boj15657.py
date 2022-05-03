# https://www.acmicpc.net/problem/15657
# N과 M (8)
from sys import stdin
import itertools

n, m = map(int, stdin.readline().split())

nums = sorted(list(map(int, stdin.readline().split())))

# 중복 조합 구하기
combs = itertools.combinations_with_replacement(nums, m)

for comb in combs:
    print(*comb)
