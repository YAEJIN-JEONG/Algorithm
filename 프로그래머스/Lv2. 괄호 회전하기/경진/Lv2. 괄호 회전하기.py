# https://programmers.co.kr/learn/courses/30/lessons/76502
def is_valid(s):
    pair = {']': '[', '}': '{', ')': '('}

    stack = []
    for c in s:
        if c in '[{(':
            stack.append(c)
        else:
            if not stack or stack.pop() != pair[c]:
                return False

    if stack:
        return False

    return True


def solution(s):
    answer = 0

    for i in range(len(s)):
        # 왼쪽으로 1회 회전
        s = s[1:] + s[0]
        if is_valid(s):
            answer += 1

    return answer
