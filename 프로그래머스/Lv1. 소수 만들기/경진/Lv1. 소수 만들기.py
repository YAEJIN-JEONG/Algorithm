# https://programmers.co.kr/learn/courses/30/lessons/12977
import itertools


def solution(nums):
    answer = 0
    # itertools -> permutation(순열), combinations(조합)
    comb_list = itertools.combinations(nums, 3)

    for comb in comb_list:
        total = sum(comb)
        for i in range(2, total // 2 + 1):
            if total % i == 0:
                break
        else:
            answer += 1

    return answer
