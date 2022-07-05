# https://www.acmicpc.net/problem/2166
# 다각형의 면적
from sys import stdin

n = int(stdin.readline())
points = [list(map(int, stdin.readline().split())) for _ in range(n)]
points.append(points[0])

# 신발끈 공식 (사선 공식)
s = 0
for i in range(len(points) - 1):
    s += points[i][0] * points[i + 1][1]

for i in range(1, len(points)):
    s -= points[i][0] * points[i - 1][1]

s = abs(s) / 2
print('%.1f' % s)
