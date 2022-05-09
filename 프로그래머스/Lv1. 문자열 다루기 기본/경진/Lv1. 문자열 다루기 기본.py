# https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False

    return True if s.isdigit() else False
