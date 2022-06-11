# https://www.acmicpc.net/problem/1562
# 계단 수
from sys import stdin

n = int(stdin.readline())

# dp[숫자길이][숫자포함여부][끝 숫자]
dp = [[[0] * 10 for _ in range(1 << 10)] for _ in range(n + 1)]

# 숫자길이가 1인 경우에 대하여 초기화
for i in range(1, 10):
    dp[1][1 << i][i] = 1

for i in range(2, n + 1):
    for bit in range(1 << 10):
        for num in range(10):
            for prev in [num - 1, num + 1]:
                if prev < 0 or prev > 9:
                    continue
                dp[i][bit | (1 << num)][num] += dp[i - 1][bit][prev]

# 길이가 n 이고, 0 ~ 9 모든 숫자가 포함된 경우
print(sum(dp[n][(1 << 10) - 1]) % int(1e9))
