# https://www.acmicpc.net/problem/15666
# N과 M (12)
from sys import stdin
import itertools

n, m = map(int, stdin.readline().split())

nums = sorted(list(map(int, stdin.readline().split())))

# 순열 구하기
combs = itertools.combinations_with_replacement(nums, m)

# 이미 출력된 순열 printed 에 저장
printed = set()
for comb in combs:
    if comb not in printed:
        print(*comb)
        printed.add(comb)
