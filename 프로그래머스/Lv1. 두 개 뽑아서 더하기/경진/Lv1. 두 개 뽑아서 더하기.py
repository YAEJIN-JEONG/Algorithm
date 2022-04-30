# https://programmers.co.kr/learn/courses/30/lessons/68644
import itertools


def solution(numbers):
    # 중복되지 않는 두 수의 합 저장
    n_set = set()
    # 두 개 뽑는 조합 구하기
    comb = itertools.combinations(numbers, 2)
    # 두 수의 합 구해서 저장
    for c in comb:
        n_set.add(sum(c))

    # 오름차순 리스트로 반환
    return sorted(list(n_set))
