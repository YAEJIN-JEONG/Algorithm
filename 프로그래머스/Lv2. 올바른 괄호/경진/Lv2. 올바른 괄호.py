# https://programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        elif not stack:
            return False
        else:
            stack.pop()

    return True if not stack else False
