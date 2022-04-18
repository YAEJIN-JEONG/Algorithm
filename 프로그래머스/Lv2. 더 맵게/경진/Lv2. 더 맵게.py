# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, k):
    # 우선순위 큐
    heapq.heapify(scoville)
    cnt = 0

    while scoville:
        s1 = heapq.heappop(scoville)
        # 제일 작은 스코빌 지수가 k 이상 이면 멈추기
        if s1 >= k:
            break
        # 스코빌 지수가 제일 작은 두 개 음식 섞기
        if scoville:
            s2 = heapq.heappop(scoville)
            heapq.heappush(scoville, s1 + s2 * 2)
            cnt += 1
    else:
        # break 에 안걸렸으면 불가능 한 것
        return -1

    return cnt
