# https://programmers.co.kr/learn/courses/30/lessons/12946
def rec(answer, n, fr, via, to):
    if n == 1:
        answer.append([fr, to])
    else:
        # 원판 두 개 이상 옮기는 법
        # fr -> via, fr -> to, via -> to
        rec(answer, n - 1, fr, to, via)
        answer.append([fr, to])
        rec(answer, n - 1, via, fr, to)


def solution(n):
    answer = []
    rec(answer, n, 1, 2, 3)
    return answer
