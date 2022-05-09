# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])

    return answer
