# https://www.acmicpc.net/problem/9375
# 패션왕 신해빈
from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())

    # 옷 종류: 개수
    clothes = {}

    for _ in range(n):
        name, category = stdin.readline().split()
        clothes[category] = clothes.get(category, 0) + 1

    total = 1
    # 옷 종류 마다 1개 뽑아서 입는 모든 경우의 수 (안 뽑는 것 포함)
    for i in clothes.values():
        total *= (i + 1)

    # 모두 안 뽑는 경우 빼줌
    print(total - 1)
