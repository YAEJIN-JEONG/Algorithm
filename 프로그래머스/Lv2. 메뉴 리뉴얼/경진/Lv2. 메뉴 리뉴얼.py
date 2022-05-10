# https://programmers.co.kr/learn/courses/30/lessons/72411
import itertools


def solution(orders, course):
    answer = []
    for n in course:
        # 조합 카운트, 제일 많이 시킨 조합 횟수
        order_cnt, max_cnt = {}, 0

        for order in orders:
            # n 개 뽑는 조합, 뽑기 전에 문자열 정렬
            for comb in itertools.combinations(sorted(list(order)), n):
                s = ''.join(comb)
                # 해당 조합 몇 번 나왔는지 카운트
                order_cnt[s] = order_cnt.get(s, 0) + 1
                max_cnt = max(max_cnt, order_cnt[s])

        # 2번 이상 시키고, 제일 많이 시킨 조합 코스 요리로 구성
        for k, v in order_cnt.items():
            if v >= 2 and v == max_cnt:
                answer.append(k)

    return sorted(answer)
