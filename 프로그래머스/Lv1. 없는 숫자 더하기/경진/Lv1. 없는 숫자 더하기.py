# https://programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    total = (9 * 10) // 2
    total_numbers = sum(set(numbers))
    return total - total_numbers
