# https://programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 0

    # n 부터 0까지 역추적 (짝수인 경우 2로 나누기, 홀수인 경우 1 빼고 2로 나누기)
    while n > 0:
        if n & 1 == 0:
            n //= 2
        else:
            n = (n - 1) // 2
            ans += 1

    return ans
