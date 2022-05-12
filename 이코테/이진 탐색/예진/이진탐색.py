# n 원소의 개수, target 찾고자 하는 값
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

def binary_search1(array,target, start,end):
    # 재귀적 구현
    if start > end :
        return None
    mid = (start+end)//2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] ==target:
        return mid
    # 중간점 값보다 찾고자 하는 값이 작은 경우 왼쪽 체크
    elif array[mid] > target :
        return binary_search1(array, target,start,mid-1)
    # 중간점 값보다 찾고자 하는 값이 큰 경우 오른쪽 체크
    else:
        return binary_search1(array,target,mid+1,end)

def binary_search2(array,target,start,end):
    # 반복문 구현
    while start <= end:
        mid = (start + end) //2
        if array[mid] == target :
            return mid
        elif array[mid] >target :
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_search1(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)