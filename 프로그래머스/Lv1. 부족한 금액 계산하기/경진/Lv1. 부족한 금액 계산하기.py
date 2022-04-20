# https://programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    total = 0
    for i in range(1, count + 1):
        total += price * i

    answer = total - money

    return answer if answer > 0 else 0
