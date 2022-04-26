# https://www.acmicpc.net/problem/11726
# 2xn 타일링
from sys import stdin

n = int(stdin.readline())

dp = [0, 1, 2, 3]

# 점화식: f(n) = f(n - 1) + f(n - 2)
for i in range(4, n + 1):
    dp.append((dp[i - 1] + dp[i - 2]) % 10007)

print(dp[n])
