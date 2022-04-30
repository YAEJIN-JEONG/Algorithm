# https://programmers.co.kr/learn/courses/30/lessons/92334
from collections import defaultdict


def solution(id_list, report, k):
    report_to = defaultdict(set)    # 신고한사람 - 신고받은사람
    report_from = defaultdict(set)  # 신고받은사람 - 신고한사람
    black_list = set()              # 정지된 사람
    answer = []

    # report 를 파싱하여 데이터 만들기
    for s in set(report):
        u1, u2 = s.split()
        report_to[u1].add(u2)
        report_from[u2].add(u1)

    # 정지된 사람 리스트
    for key in report_from.keys():
        if len(report_from[key]) >= k:
            black_list.add(key)

    # 문제에서 요구하는 정보 만들기
    for u in id_list:
        answer.append(len(report_to.get(u, set()) & black_list))

    return answer
