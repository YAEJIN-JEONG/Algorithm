# https://programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer, increment = [], x

    for i in range(n):
        answer.append(x)
        x += increment

    return answer
