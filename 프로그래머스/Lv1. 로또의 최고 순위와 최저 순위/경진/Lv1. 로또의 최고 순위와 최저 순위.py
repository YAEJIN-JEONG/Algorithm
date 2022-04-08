# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    # 맞힌 개수에 따른 순위
    rank = [6, 6, 5, 4, 3, 2, 1]
    # 0 개수
    zero_count = lottos.count(0)
    # 최소 맞힌 개수
    low = len(set(lottos) & set(win_nums))

    return [rank[low + zero_count], rank[low]]
