# https://programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    answer = ''

    for c in s:
        if c == ' ':
            answer += c
        else:
            start = 'A'
            if 'a' <= c <= 'z':
                start = 'a'

            answer += chr((ord(c) - ord(start) + n) % 26 + ord(start))

    return answer
