# https://www.acmicpc.net/problem/11660
# 구간 합 구하기 5
from sys import stdin

n, m = map(int, stdin.readline().split())
array = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

# (1, 1) ~ (i, j) 까지의 구간 합을 미리 저장
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # (1, 1) ~ (i, j) 까지의 구간 합은
        # (1, 1) ~ (i - 1, j) 구간 합 + (1, 1) ~ (i, j - 1) 구간 합에
        # (1, 1) ~ (i - 1, j - 1) 구간 합을 빼고 (중복 값 빼기), 현재 값 더하면 됨
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]) + array[i - 1][j - 1]

answer = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    answer.append(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1]))

print('\n'.join(map(str, answer)))
