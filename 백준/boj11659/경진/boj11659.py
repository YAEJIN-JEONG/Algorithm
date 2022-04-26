# https://www.acmicpc.net/problem/11659
# 구간 합 구하기 4
from sys import stdin

n, m = map(int, stdin.readline().split())
n_seq = list(map(int, stdin.readline().split()))

# sub_total 의 n 번째 원소는 n_seq 의 n 번째 원소까지의 합
sub_total = [n_seq[0]]
for x in range(1, n):
    sub_total.append(sub_total[x - 1] + n_seq[x])

for _ in range(m):
    i, j = map(int, stdin.readline().split())
    print(sub_total[j - 1] - (sub_total[i - 2] if i - 2 >= 0 else 0))
