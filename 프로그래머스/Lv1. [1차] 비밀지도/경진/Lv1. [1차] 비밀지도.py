# https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 비트 연산 -> 결과 값에서 0b 제거 -> left padding 0 으로 채우기 -> 1은 '#'으로 0은 ' '으로
        answer.append(bin(arr1[i] | arr2[i])[2:].rjust(n, '0').replace('1', '#').replace('0', ' '))

    return answer
