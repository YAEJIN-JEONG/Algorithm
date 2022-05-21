# NxM으로 놓인 카드를 입력받고
# 행에서 가장 작은 수 가운데 가장 큰수
n,m = map(int,input().split())
min_value = []

for i in range(n):
    data =list(map(int,input().split()))
    min_value.append(min(data))

result = max(min_value)
print(result)