# https://programmers.co.kr/learn/courses/30/lessons/12940
import math


def solution(n, m):
    return [math.gcd(n, m), n * m // math.gcd(n, m)]
