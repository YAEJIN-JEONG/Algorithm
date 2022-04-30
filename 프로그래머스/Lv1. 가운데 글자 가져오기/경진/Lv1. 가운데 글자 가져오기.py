# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    # 길이가 홀수이면 가운데 한 글자, 짝수이면 가운데 두 글자
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1:len(s) // 2 + 1]
