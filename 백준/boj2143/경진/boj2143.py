# https://www.acmicpc.net/problem/2143
# 두 배열의 합
from sys import stdin
from bisect import bisect_left, bisect_right

t = int(stdin.readline())
n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
B = list(map(int, stdin.readline().split()))

# 부분 배열의 합
# sub_total[0] = A 부분 배열의 합
# sub_total[1] = B 부분 배열의 합
sub_total = [A[:], B[:]]

for i in range(n):
    total = A[i]
    for j in range(i + 1, n):
        total += A[j]
        sub_total[0].append(total)

for i in range(m):
    total = B[i]
    for j in range(i + 1, m):
        total += B[j]
        sub_total[1].append(total)

for sub in sub_total:
    sub.sort()

answer = 0
for i in sub_total[0]:
    target = t - i
    answer += bisect_right(sub_total[1], target) - bisect_left(sub_total[1], target)

print(answer)
