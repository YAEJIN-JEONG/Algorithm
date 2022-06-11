# https://www.acmicpc.net/problem/1509
# 팰린드롬 분할
from sys import stdin

s = stdin.readline().rstrip()
size = len(s)

# dp[i][j] 는 s[i:j + 1] 의 팰린드롬 여부
dp = [[False] * size for _ in range(size)]

for i in range(size):
    dp[i][i] = True

# j ~ j + i 번째 문자 단위로 판별
# 작은 길이부터 길이 순서대로 진행
for i in range(1, size):
    for j in range(size - i):
        if s[j] == s[j + i] and (i == 1 or dp[j + 1][j + i - 1]):
            dp[j][j + i] = True

# dp2[i] 는 i 번째 문자 까지의 최소 분할갯수
dp2 = [i + 1 for i in range(size)]
for i in range(1, size):
    # 다음 문자를 추가했을 때, 새로운 팰린드롬이 생기지 않는 경우
    dp2[i] = dp2[i - 1] + 1
    for j in range(i):
        if dp[j][i]:
            # j 가 0 이면 i 번째 까지의 문자열 전체가 팰린드롬, 아니면 이전 단계 + 1
            dp2[i] = min(dp2[i], dp2[j - 1] + 1) if j > 0 else 1

print(dp2[-1])
