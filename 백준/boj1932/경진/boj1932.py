# https://www.acmicpc.net/problem/1932
# 정수 삼각형
from sys import stdin

n = int(stdin.readline())
triangle = [[i for i in map(int, stdin.readline().split())] for _ in range(n)]
# dp 배열에 해당 위치까지의 최대값만 저장하면서 진행
dp = [[0 for i in range(j + 1)] for j in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i + 1):
        # 가장 앞쪽
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        # 가장 뒷쪽
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        # 나머지 (중간)
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

print(max(dp[n - 1]))
