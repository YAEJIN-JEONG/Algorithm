# 수박수박수박수박수박수?
def solution(n):
    answer = '수박' * (n // 2)
    return answer + '수' if n % 2 == 1 else answer
