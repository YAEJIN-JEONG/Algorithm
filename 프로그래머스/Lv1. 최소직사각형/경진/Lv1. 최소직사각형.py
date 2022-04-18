# https://programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    # 가로, 세로 중에 큰 값을 가로, 작은 값을 세로로 생각
    # 각 가로, 세로의 최대값으로 지갑만들면 됨
    w_list, h_list = [], []

    for size in sizes:
        size.sort()
        w_list.append(size[0])
        h_list.append(size[1])

    return max(w_list) * max(h_list)
