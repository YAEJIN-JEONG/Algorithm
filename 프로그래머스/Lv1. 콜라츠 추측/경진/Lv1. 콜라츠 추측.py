# https://programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    answer = 0

    while answer <= 500 and num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1

        answer += 1

    return answer if answer <= 500 else -1
