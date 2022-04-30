# https://www.acmicpc.net/problem/2579
from sys import stdin

n = int(stdin.readline())

score = []
for _ in range(n):
    score.append(int(stdin.readline()))

# f(0) = score(0)
# f(1) = score(0) + score(1)
# f(2) = max(score(0) + score(2), score(1) + score(2))
# 점화식: f(x) = max(score(x) + score(x-1) + f(x-3), score(x) + f(x-2))

dp = [score[0]]

if n > 1:
    dp.append(score[0] + score[1])
if n > 2:
    dp.append(max(score[0] + score[2], score[1] + score[2]))
    for i in range(3, n):
        dp.append(max(score[i] + score[i-1] + dp[i-3], score[i] + dp[i-2]))

print(dp[n - 1])
