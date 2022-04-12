# https://programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque


def solution(progresses, speeds):
    answer = []
    # 작업 진도, 작업 속도 큐 만들기
    progresses_q, speeds_q = deque(progresses), deque(speeds)
    # cnt: 배포되는 작업 수, days: 며칠 지났는지
    cnt, days = 0, 0

    while progresses_q:
        speed = speeds_q.popleft()
        # 작업 진도 = 기존 작업 진도 + (작업 속도 * 지난 날짜)
        progress = progresses_q.popleft() + speed * days

        if progress >= 100:
            cnt += 1
        else:
            # 며칠이 더 지나야 작업이 완료되는지 계산하여 더함
            days += (100 - progress - 1) // speed + 1
            if cnt > 0:
                answer.append(cnt)
            cnt = 1
    # 마지막으로 추가되지 않은 배포작업 수 추가
    answer.append(cnt)

    return answer
