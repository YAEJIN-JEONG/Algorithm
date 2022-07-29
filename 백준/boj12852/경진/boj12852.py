# https://www.acmicpc.net/problem/12852
# 1로 만들기 2
from sys import stdin

n = int(stdin.readline())

# dp
dp = [i for i in range(n + 1)]

for i in range(2, n + 1):
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    dp[i] = min(dp[i], dp[i - 1] + 1)

answer, k = [n], n
# 역추적
while k > 1:
    if dp[k] == dp[k - 1] + 1:
        k -= 1
    elif k % 2 == 0 and dp[k] == dp[k // 2] + 1:
        k //= 2
    elif k % 3 == 0 and dp[k] == dp[k // 3] + 1:
        k //= 3

    answer.append(k)

print(dp[-1] - 1)
print(' '.join(map(str, answer)))
