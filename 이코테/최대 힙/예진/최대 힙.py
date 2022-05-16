import heapq

# 내림차순 정렬
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        # 데이터를 힙에 넣기 전에 부호를 바꿔서 넣음
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        # 데이터를 꺼낼 때 부호를 바꿔서 꺼냄
        result.append(-heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)