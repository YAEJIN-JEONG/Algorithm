# https://programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    dp = [0, 1, 2]

    for i in range(3, n + 1):
        # i - 1 까지 가는 경우의 수 + (1 걸음 더 가기)
        # i - 2 까지 가는 경우의 수 + (2 걸음 더 가기)
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n] % 1234567
