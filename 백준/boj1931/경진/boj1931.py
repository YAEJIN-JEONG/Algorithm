# https://www.acmicpc.net/problem/1931
from sys import stdin

n = int(stdin.readline())
n_list = []

for _ in range(n):
    s, e = map(int, stdin.readline().split())
    n_list.append((s, e))
# 회의 종료가 빠른 순서대로
# 시작과 종료가 같은 회의도 있을 수 있음
# -> 종료 시각이 같으면 시작이 빠른 순서대로
n_list.sort(key=lambda x: x[0])
n_list.sort(key=lambda x: x[1])

answer, time = 0, 0
for s, e in n_list:
    if s >= time:
        answer += 1
        time = e

print(answer)
