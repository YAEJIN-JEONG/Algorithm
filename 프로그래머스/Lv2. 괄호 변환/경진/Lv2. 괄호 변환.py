# https://programmers.co.kr/learn/courses/30/lessons/60058
# 문제에 나온 설명대로 차례대로 구현
def rec(u, v):
    if u == '':
        return u

    u2, v2 = divide(v)

    if check(u):
        return u + rec(u2, v2)
    else:
        result = '(' + rec(u2, v2) + ')'

        for c in u[1:-1]:
            result += ')' if c == '(' else '('

        return result


# s가 올바른 괄호 문자열인지 체크
def check(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


# s를 더 이상 나눌 수 없는 '균형잡힌 괄호 문자열' u와 나머지 v로 나누기
def divide(s):
    count = {'(': 0, ')': 0}

    for i in range(len(s)):
        count[s[i]] += 1

        if count['('] > 0 and count['('] == count[')']:
            return s[:i + 1], s[i + 1:]

    return s, ''


def solution(p):
    if len(p) == 0:
        return p

    u, v = divide(p)
    return rec(u, v)
