# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기
from sys import stdin

t = int(stdin.readline())

dp = [0, 1, 2, 4]
for _ in range(t):
    n = int(stdin.readline())

    # 더할 수 있는 수는 [1, 2, 3]
    # (n - 1) + 1, (n - 2) + 2, (n - 3) + 3 이 가능
    # 점화식: f(n) = f(n - 1) + f(n - 2) + f(n - 3)
    for i in range(len(dp), n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    print(dp[n])
