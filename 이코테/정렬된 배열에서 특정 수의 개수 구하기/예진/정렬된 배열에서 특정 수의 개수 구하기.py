from bisect import bisect_left, bisect_right

# N 수열의 개수 x 찾고자 하는 값
N, x = map(int, input().split())

# 수열 N의 원소(오름차순 정렬된 상태)
array = list(map(int, input().split()))

# 값이 [x,x] 범위에 있는 데이터 개수 계산
def count_by_range(array,x):
    # bisect_right : 배열에 x 를 삽입할 가장 오른쪽 인덱스 반환
    right_index = bisect_right(array, x)
    # bisect_left : 배열에 x를 삽입할 가장 왼쪽 인덱스 반환
    left_index = bisect_left(array, x)
    return right_index - left_index

result = count_by_range(array,x)

# 값이 x인 원소가 존재하지 않으면 -1 출력
if result == 0:
    print(-1)
# 값이 x인 원소 존재
else :
    print(result)
