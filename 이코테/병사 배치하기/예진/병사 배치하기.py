# 가장 긴 증가하는 부분수열 Longest Increasing Subsequence LIS
# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 모든 0 <= j < i 에 대하여, D[i] = max(D[i],D[j]+1) if array[j] < array[i]

# n 명의 병사
n = int(input())
# 각 병사의 전투력
array = list(map(int,input().split()))

# 순서를 뒤집어 최장 증가 부분 수열 문제로 변환
array.reverse()

# dp위한 1차원 테이블로 초기화
dp = [1] * n

# LIS 수행
# 2번째 원소부터 마지막 원소까지 각 원소를 확인
for i in range(1,n):
    for j in range(0,i):
        #앞에 있는 원소 중 해당 원소가 자기보다 작은 경우 갱신
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)


# 열외해야 하는 병사의 최소 수 출력
# max(dp) 가장 긴 부분 수열의 길이
print(n - max(dp))