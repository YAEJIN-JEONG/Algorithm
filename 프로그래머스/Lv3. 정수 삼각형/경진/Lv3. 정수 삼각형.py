# https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    dp = [[0 for _ in range(j + 1)] for j in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    # 꼭대기 부터 층마다 최댓값 저장
    for i in range(1, len(dp)):
        # 맨 앞과 맨 뒤는 따로 처리
        for j in range(i + 1):
            if j == 0:      # 맨 앞
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:    # 맨 뒤
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:           # 나머지
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

    return max(dp[len(triangle) - 1])
