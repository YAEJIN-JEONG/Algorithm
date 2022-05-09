# https://programmers.co.kr/learn/courses/30/lessons/12934
def solution(n):
    return (int(n ** 0.5) + 1) ** 2 if (n ** 0.5).is_integer() else -1
