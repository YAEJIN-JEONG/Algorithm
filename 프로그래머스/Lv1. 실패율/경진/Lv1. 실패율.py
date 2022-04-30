# https://programmers.co.kr/learn/courses/30/lessons/42889
from collections import Counter


def solution(n, stages):
    # stage: count 형태로 만듬
    counter = Counter(stages)
    answer, rate = [], {}

    for stage in range(1, n + 1):
        total = 0
        for i in range(stage, n + 2):
            total += counter[i]
        # 조건에 따라 실패율 stage: percentage 형태의 rate 만듬
        if counter[stage] == 0 and total == 0:
            rate[stage] = 0
        elif total == 0:
            rate[stage] = 100
        else:
            rate[stage] = counter[stage] / total

    # 값을 기준으로 역순 정렬, key 리스트 반환
    return sorted(rate, key=lambda x: rate[x], reverse=True)
