# https://www.acmicpc.net/problem/18111
# 마인크래프트
from sys import stdin
from collections import Counter

n, m, b = map(int, stdin.readline().split())

ground = []
for _ in range(n):
    ground.extend(list(map(int, stdin.readline().split())))

# 땅의 높이(key): 개수(value)
counter = Counter(ground)
low, high = min(counter.keys()), max(counter.keys())

time, height = 256 * 500 * 500, -1

for i in range(low, high + 1):
    x, y = 0, 0   # 파내야 되는 블록, 쌓아야 되는 블록

    for k, v in counter.items():
        diff = (k - i) * v

        if diff >= 0:
            x += diff
        else:
            y -= diff

    if x + b < y:
        continue

    now = 2 * x + y
    if time >= now:
        time = now
        height = i

print(time, height)
