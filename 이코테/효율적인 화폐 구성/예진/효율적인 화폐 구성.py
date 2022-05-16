# N 종류의 화폐, M 가치의 합
n,m = list(map(int, input().split()))
# n개의 각 화폐의 가치
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
# M 최대 10000
# 0원부터 m원까지 각각의 금액에 대한 최소 원의 화폐값을 구하기 위해 m+1로 화폐값 초기화
d = [10001] * (m+1)

d[0] = 0
# i 각 화폐 단위
for i in range(n):
    # j 각 화폐의 금액
    for j in range(array[i], m+1):
        #(i-k)원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            d[j] = min(d[j],d[j - array[i]] + 1)

# 결과 출력
# 최종적으로 방법이 없는 경우
if d[m] == 10001:
    print(-1)
else :
    print(d[m])


