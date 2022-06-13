# 기존의 소수 판별
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수 체크
    for i in range(2,x):
        if x % i== 0 :
            return False
    return True

# 개선된 소수 판별
import math

def better_prime_number(x):
    # 2부터 x의 제곱급까지의 모든 수를 체크
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
