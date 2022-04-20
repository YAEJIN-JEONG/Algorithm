# https://programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):
    answer = -1

    for i in range(2, n):
        if n % i == 1:
            answer = i
            break

    return answer
