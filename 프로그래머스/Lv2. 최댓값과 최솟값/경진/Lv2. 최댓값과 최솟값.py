# https://programmers.co.kr/learn/courses/30/lessons/12939
# 최댓값과 최솟값
def solution(s):
    n_list = sorted(list(map(int, s.split())))
    return ' '.join(map(str, [n_list[0], n_list[-1]]))
