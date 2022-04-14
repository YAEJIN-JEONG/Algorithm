# https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    return min(len(nums) // 2, len(set(nums)))
