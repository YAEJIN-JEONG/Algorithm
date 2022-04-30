# https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []

    for command in commands:
        n_array = array[command[0] - 1: command[1]]
        n_array.sort()
        answer.append(n_array[command[2] - 1])

    return answer
