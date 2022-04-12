# https://programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    # 데이터 크기나 수가 매우 크다면 이분탐색 의심하기
    low, high = 1, max(times) * 1000000000

    # 가장 작은 값 찾아야 함 -> lower bound
    while low <= high:
        mid = (low + high) // 2
        total = 0

        for time in times:
            total += mid // time

        # 값이 같으면 high 를 바꾸어 low 는 고정 -> lower bound
        if total >= n:
            high = mid - 1
        else:
            low = mid + 1

    return low
