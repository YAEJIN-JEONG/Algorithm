from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    # bisect_right(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환
    right_index = bisect_right(a, right_value)
    # bisect_left(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1, 2, 3 ,3, 3, 3, 4, 4, 8, 9]

#값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))
#값이 [-1,3] 범위의 데이터 개수 출력
print(count_by_range(a ,-1, 3))