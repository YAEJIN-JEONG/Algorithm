# https://www.acmicpc.net/problem/11054
# 가장 긴 바이토닉 부분 수열
from sys import stdin

n = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))

# 수열의 처음부터 증가하는 부분 수열 최대 길이 dp
l_dp = [1] * n
# 수열의 오른쪽부터 증가하는 부분 수열 최대 길이 dp
r_dp = [1] * n

# 0 ~ n
for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            l_dp[i] = max(l_dp[i], l_dp[j] + 1)

# n ~ 0
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if seq[j] < seq[i]:
            r_dp[i] = max(r_dp[i], r_dp[j] + 1)

# dp 값을 인덱스에 맞게 합치고, 자기 자신이 중복되었으므로 1뺌
for i in range(n):
    l_dp[i] += r_dp[i] - 1

print(max(l_dp))
