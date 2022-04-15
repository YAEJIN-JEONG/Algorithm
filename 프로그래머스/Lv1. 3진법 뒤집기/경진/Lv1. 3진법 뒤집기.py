# https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    # 3진법 만들기
    k = ''
    while n > 0:
        k = str(n % 3) + k
        n //= 3

    # 뒤집힌 10진법 만들기
    answer = 0
    for i in range(len(k)):
        answer += int(k[i]) * (3 ** i)

    return answer
