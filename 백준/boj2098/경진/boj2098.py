# https://www.acmicpc.net/problem/2098
# 외판원 순회
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
# dp[v][visit] = 0번에서 visit 의 도시들 순회 후, v에 도착할 때의 최소 비용
dp = [[1 << 32] * (1 << n) for _ in range(n)]
dp[0][0] = 0

for visit in range(1 << n):
    for v1 in range(n):
        for v2 in range(n):
            if (visit & (1 << v2)) > 0 and w[v2][v1] != 0:
                dp[v1][visit] = min(dp[v1][visit], dp[v2][visit & (~(1 << v2))] + w[v2][v1])

print(dp[0][-1])
