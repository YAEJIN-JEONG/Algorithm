# https://programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    s = s.lower()
    return True if s.count('p') == s.count('y') else False
