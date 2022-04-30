# https://www.acmicpc.net/problem/11727
# 2xn 타일링 2
from sys import stdin

n = int(stdin.readline())

dp = [0, 1, 3]

# 점화식: f(n) = f(n - 1) + 2 * f(n - 2)
for i in range(3, n + 1):
    dp.append((dp[i - 1] + dp[i - 2] * 2) % 10007)

print(dp[n])
