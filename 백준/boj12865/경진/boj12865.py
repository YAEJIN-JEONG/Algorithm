# https://www.acmicpc.net/problem/12865
# 평범한 배낭
from sys import stdin

n, k = map(int, stdin.readline().split())

items = []
for _ in range(n):
    w, v = map(int, stdin.readline().split())
    items.append((w, v))

# dp[i][j] 에는 담을 수 있는 무게가 j 일 때, i 번째 아이템 까지 본 경우 최대 가치
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for weight in range(1, k + 1):
        now_weight, now_value = items[i - 1]
        # 현재 무게가 아이템 무게 보다 작으면, 현재 무게에서 이전 아이템까지 넣은 가치가 최대
        # 그렇지 않으면
        # 탐색중인 무게에서 아이템 무게 뺀 만큼의 무게에서 넣을 수 있는 최대 가치 + 아이템 가치
        # 이번 아이템 안챙기기 (이전 아이템까지 넣은 가치)
        # 중에 큰 것
        if weight < now_weight:
            dp[i][weight] = dp[i - 1][weight]
        else:
            dp[i][weight] = max(dp[i - 1][weight - now_weight] + now_value, dp[i - 1][weight])

print(dp[n][k])
