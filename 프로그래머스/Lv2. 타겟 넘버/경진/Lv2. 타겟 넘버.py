# https://programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque


def solution(numbers, target):
    answer = 0
    # bfs
    deq = deque()
    # index, sum 튜플 입력
    deq.append((0, 0))

    while deq:
        i, n = deq.popleft()
        # index 가 numbers 크기와 같으면 연산이 완료된 것
        if i == len(numbers):
            if n == target:
                answer += 1
        else:
            deq.append((i + 1, n + numbers[i]))
            deq.append((i + 1, n - numbers[i]))

    return answer
