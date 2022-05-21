n,m,k = map(int,input().split())
array = list(map(int, input().split()))

array.sort()
first = array[n-1]
second = array[n-2]

result = 0

# 가장 큰 수가 더해지는 횟수 계산
# 가장 큰수 k번 두번째로 큰수 한번 더하는 연산 반복이므로
count = int(m / (k+1)) * k
# 나누어 떨어지지 않는 경우 나머지 더하기
count += m %(k+1)

result += count*first
result += (m-count)*second

print(result)