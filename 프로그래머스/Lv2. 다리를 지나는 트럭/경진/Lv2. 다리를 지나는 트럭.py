# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


def solution(bridge_length, weight, truck_weight):
    # 다리 길이만큼 0 추가
    deq = deque([0 for _ in range(bridge_length)])
    curr_weight, answer = 0, 0

    while True:
        curr_weight -= deq.pop()

        if truck_weight:
            now = truck_weight[0]
            # 현재 트럭이 다리에 올라갈 수 있으면 올리기
            if curr_weight + now <= weight:
                deq.appendleft(truck_weight.pop(0))
                curr_weight += now
            else:
                deq.appendleft(0)

        answer += 1
        if curr_weight == 0:
            break

    return answer
