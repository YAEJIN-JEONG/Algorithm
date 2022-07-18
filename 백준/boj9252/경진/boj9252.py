# https://www.acmicpc.net/problem/9252
# LCS 2
a, b = input(), input()
n, m = len(a) + 1, len(b) + 1
# 최장 공통 부분 수열 dp
dp = [[0] * m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# trace
pos, lcs = [len(dp) - 1, len(dp[0]) - 1], ''
while dp[pos[0]][pos[1]] > 0:
    now = dp[pos[0]][pos[1]]
    while now == dp[pos[0] - 1][pos[1]]:
        pos[0] -= 1
    while now == dp[pos[0]][pos[1] - 1]:
        pos[1] -= 1

    lcs = a[pos[0] - 1] + lcs
    pos[0], pos[1] = pos[0] - 1, pos[1] - 1

print(dp[-1][-1])
print(lcs)
