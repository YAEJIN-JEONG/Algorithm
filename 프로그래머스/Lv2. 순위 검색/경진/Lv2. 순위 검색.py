# https://programmers.co.kr/learn/courses/30/lessons/72412
from collections import defaultdict
import bisect


def solution(info, query):
    # 해쉬 테이블
    info_map = defaultdict(list)

    for inf in info:
        s = inf.split()
        # 0000 ~ 1111, 네 가지 항목에 대해 1이면 포함 0이면 미포함('-')
        for i in range(1 << 4):
            # 0001, 0010, 0100, 1000 와 &연산 하여 포함 여부 결정
            info_map[''.join([s[j] if (1 << j) & i != 0 else '-' for j in range(4)])].append(int(s[4]))

    # 이분 탐색 위해 정렬
    for v in info_map.values():
        v.sort()

    answer = []
    for q in query:
        lang, _, category, _, career, _, soul_food, score = q.split()

        rs = info_map[lang + category + career + soul_food]
        # 코딩 테스트 점수에 대한 lower_bound 찾기
        lower_bound = bisect.bisect_left(rs, int(score))

        # lower_bound 위쪽 부분 세기
        answer.append(len(rs) - lower_bound)

    return answer
