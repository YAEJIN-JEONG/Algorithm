# https://programmers.co.kr/learn/courses/30/lessons/17687

# k를 base 진법으로 표현
def convert(k, base):
    result, num = '', '0123456789ABCDEF'

    while k > 0:
        k, mod = divmod(k, base)
        result = num[mod] + result

    return result


def solution(n, t, m, p):
    # 구해야 하는 총 길이
    size = p + m * t

    s, k = '0', 1
    while len(s) < size:
        s += convert(k, n)
        k += 1

    # 튜브가 말해야 하는 차례 t개
    return ''.join([s[p + m * i - 1] for i in range(t)])
