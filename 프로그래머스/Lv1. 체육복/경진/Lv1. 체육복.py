# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    lost, reserve = set(lost), set(reserve)
    # 체육복 여벌이 있는 사람과, 아예 없는 사람 집합 만들기
    n_reserve = reserve - lost
    n_lost = lost - reserve
    # 여벌이 있는 사람만 빌려줄 수 있음
    for i in sorted(list(n_reserve)):
        # 번호순 정렬 후, 앞 사람 빌려줄 수 있는지 먼저 확인
        if i - 1 in n_lost:
            n_lost.remove(i - 1)
        elif i + 1 in n_lost:
            n_lost.remove(i + 1)

    return n - len(n_lost)
