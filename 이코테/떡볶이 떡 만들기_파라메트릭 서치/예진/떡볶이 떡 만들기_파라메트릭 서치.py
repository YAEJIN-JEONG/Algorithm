# n 떡의 개수 m 떡의 길이
n,m = list(map(int,input().split()))
# hight 떡의 개별 높이
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점 끝점 설정
start = 0
end = max(array)
result = 0

while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid :
            total += x - mid
    # 부족한 경우 더 많이 자르기 -> 왼쪽 탐색
    if total < m :
        end = mid - 1
    # 떡이 남는 경우 덜 자르기 -> 오른쪽 탐색
    else :
        result = mid
        start = mid + 1

print(result)