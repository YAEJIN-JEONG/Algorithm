# array[i][j] : i행 j열에 존재하는 금의 양
# dp[i][j] : i행 j열까지의 최적의 해 (얻을 수 있는 금의 최댓값)

# 고려하는 경우
# 왼쪽 위에서 오는 경우 : dp[i-1][j-1]
# 왼쪽 아래에서 오는 경우 : dp[i+1][j-1]
# 왼쪽에서 오는 경우 : dp[i][j-1]

# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]

# 테스트 케이스 tc
for tc in range(int(input())):
    # n x m 크기의 금광 (1 <= n , m <= 20)
    n,m = map(int,input().split())
    array = list(map(int,input().split()))

    # dp위한 2차원 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        # 열의 크기 m단위로 데이터를 슬라이싱해서 dp 테이블에 담음
        dp.append(array[index:index + m])
        index += m

    # dp start , j는 열 기준
    for j in range(1, m):
        # i 각 행 확인
        for i in range(n):
            # 왼쪽 위에서 오는 경우 : dp[i-1][j-1]
            # index 벗어나는지 체크
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우 : dp[i+1][j-1]
            # index 벗어나는지 체크
            if i == n-1 :
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우 : dp[i][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
    result = 0
    for i in range(n):
        result = max(result,dp[i][m-1])
    print(result)