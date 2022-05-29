#lis문제
#원소중 본인보다 작은 원소가 있다면 +1
n = int(input())
a = list(map(int, input().split()))
dp = [1 for i in range(n)]  #본인을 포함해서 1부터 시작


for i in range(n):  #모든 원소를 탐색
    for j in range(i):      #현제 원소까지 탐색
        if a[j] < a[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
print(dp)