# https://programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = []
    for elem in sorted(arr):
        if elem % divisor == 0:
            answer.append(elem)

    return answer if len(answer) > 0 else [-1]
