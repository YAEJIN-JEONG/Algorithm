import re, math

def solution(n, k):
    REGEX = re.compile("[1-9]+")
    
    def convert(n, k):
        data = []
        while n:
            n, remain = n//k, n%k
            data.append(str(remain))
        return ''.join(reversed(data))

    def is_prime(number):
        if number == 1: return False
        for i in range(2, int(math.sqrt(number)+1)):
            if number % i == 0: return False
        return True
        
    def primes(number):
        result = 0
        for candidate in re.findall(REGEX, number):
            result += is_prime(int(candidate))
        return result
        
    return primes(convert(n, k))
