# https://www.acmicpc.net/problem/2467
# 용액
from sys import stdin

n = int(stdin.readline())
n_list = list(map(int, stdin.readline().split()))

# 0에 가장 가까운 혼합값, 숫자 a, 숫자 b, left pointer, right pointer
nearest, a, b, lp, rp = 1 << 32, -1, -1, 0, n - 1

# 투 포인터
while lp < rp:
    now = n_list[lp] + n_list[rp]

    if nearest > abs(now):
        nearest = abs(now)
        a, b = n_list[lp], n_list[rp]

    if now < 0:
        lp += 1
    else:
        rp -= 1

print(a, b)
