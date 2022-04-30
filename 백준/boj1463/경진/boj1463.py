# https://www.acmicpc.net/problem/1463
from sys import stdin

n = int(stdin.readline())

# 초기 값 (0번 인덱스 사용x)
dp = [0, 0, 1, 1]

# +1, x2, x3 에 대하여 dp 리스트 채워나가기
for i in range(4, n + 1):
    dp.append(dp[i-1] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
