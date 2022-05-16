# 식량창고 개수 N을 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위해 DP 테이블 초기화
# N이 최대 100 이므로, 최대 100만큼의 리스트 생성
d = [0]*100

# 다이나믹 프로그래밍 진행
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1],d[i-2]+array[i])

print(d[n-1])