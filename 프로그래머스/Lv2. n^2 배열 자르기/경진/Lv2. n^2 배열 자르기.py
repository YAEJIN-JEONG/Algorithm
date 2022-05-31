# https://programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    # 행과 열을 통해 어떤 숫자가 들어갈 지 계산.
    return [max(i // n, i % n) + 1 for i in range(left, right + 1)]
