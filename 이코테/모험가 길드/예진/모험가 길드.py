n = int(input())
person = list(map(int, input().split()))
person.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

#낮은 공포도 부터 확인
for i in person:
    #현재 그룹에 해당 모험가 포함
    count +=1
    # 현재 그룹에 해당 모험가의 수가 현재 공포도 이상이라면 그룹 결성
    if count >= i :
        result += 1 #그룹 결성
        count = 0 #현재 그룹의 모험가 초기화

print(result)