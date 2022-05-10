# https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    stack = []

    for c in s:
        # 스택 최상단 문자와 같으면 짝지어 제거
        if stack and stack[-1] == c:
            stack.pop()
            continue
        # 아니면 스택에 입력
        stack.append(c)

    return 1 if len(stack) == 0 else 0
