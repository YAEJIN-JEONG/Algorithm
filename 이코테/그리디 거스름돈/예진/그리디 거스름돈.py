# 전체 금액
n = 1260
count = 0

# 큰 단위의 화폐부터 차례로 확인
coin_types = [500,100,50,10]

# 화폐의 종류만큼 반복 수행하여 시간 복잡도만큼 수행
for coin in coin_types:
    count += n //coin # 해당 화폐로 거슬러 줄 수 있는 동전의 갯수
    n %= coin

print("거스름돈 갯수:",count)