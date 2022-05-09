# https://programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) > 0 else [-1]
