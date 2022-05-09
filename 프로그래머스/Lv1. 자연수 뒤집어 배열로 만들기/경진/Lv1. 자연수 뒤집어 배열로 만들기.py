# https://programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    return list(map(int, reversed(list(str(n)))))
