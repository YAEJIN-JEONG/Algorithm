# https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    return [[a + b for a, b in zip(c, d)] for c, d in zip(arr1, arr2)]
