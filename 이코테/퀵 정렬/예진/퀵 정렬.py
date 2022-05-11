#파이썬의 리스트 슬라이싱과 리스트 컴프리헨션을 활용한 퀵 정렬
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array)<=1:
        return array
    pivot = array[0] #첫 번째 원소를 피벗값으로 설정
    tail = array[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

def quick_sort_before(array, start, end):
    if start >= end:#원소 1개인 경우 종료
        return
    pivot = start
    left = start +1
    right = end
    while(left <= right ):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <=end and array[left] <=array[pivot]):
            left += 1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >=array[pivot]):
            right -= 1
        if(left > right):#엇갈린 경우 작은데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:#엇갈리지 경우 작은 데이터와 큰 데이터 교체
            array[left],array[right] = array[right],array[left]
    #분할 이후 왼쪽 부분과 오른쪽 부분 각각 정렬
    quick_sort_before(array,start,right-1)
    quick_sort_before(array,right+1,end)
quick_sort_before(array, 0, len(array)-1)


print(quick_sort(array))