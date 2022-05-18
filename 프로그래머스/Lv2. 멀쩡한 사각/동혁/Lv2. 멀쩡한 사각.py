def solution(w,h):
    # x * y - ( x + y - 최대 공약수)
    #ex) (8,12) 96  - (8 + 12 - 4) = 18
    #ex) (5,5) 25 - (5 + 5 -5) = 20
    from math import gcd
    answer = w*h
    g = gcd(w,h)
    return answer - (w+h-g)