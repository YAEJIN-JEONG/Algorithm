# https://programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product


def solution(word):
    alpha, dictionary = ['A', 'E', 'I', 'O', 'U'], []

    # 모든 경우 찾기 (중복 순열)
    for i in range(1, 6):
        dictionary.extend(list(map(lambda x: ''.join(x), product(alpha, repeat=i))))

    # 사전순 정렬
    dictionary.sort()

    return dictionary.index(word) + 1
