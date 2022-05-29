# https://programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    convert, zero = 0, 0

    while int(s) != 1:
        convert += 1
        zero += s.count('0')
        s = bin(len(s.replace('0', '')))[2:]

    return [convert, zero]
