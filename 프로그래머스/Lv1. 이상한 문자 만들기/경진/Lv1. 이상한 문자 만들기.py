# https://programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    answer, idx = '', 0

    # 문자 하나씩 확인
    for c in s:
        # 공백이면 idx 초기화
        if c == ' ':
            answer += c
            idx = 0
            continue

        if idx % 2 == 0:
            answer += c.upper()
        else:
            answer += c.lower()

        idx += 1

    return answer
