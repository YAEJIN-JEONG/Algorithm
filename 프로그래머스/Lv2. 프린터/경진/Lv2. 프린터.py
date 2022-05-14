# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    deq = deque(priorities)

    answer = 0
    while deq:
        now = deq.popleft()
        location -= 1

        # 큐 내에 방금 꺼낸거 보다 우선순위가 높은게 있는지에 따라 분기
        if deq and max(deq) > now:
            deq.append(now)
            if location == -1:
                location = len(deq) - 1
        else:
            answer += 1
            if location == -1:
                break

    return answer
