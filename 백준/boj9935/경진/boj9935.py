# https://www.acmicpc.net/problem/9935
# 문자열 폭발
from sys import stdin

s = stdin.readline().rstrip()
b = stdin.readline().rstrip()

result = []
for c in s:
    # 문자를 하나씩 스택에 추가
    result.append(c)
    # 추가된 문자가 폭탄 문자열의 마지막 문자이면 폭탄일 가능성 있음
    # 폭탄이 있는지 확인. 폭탄 문자열이면 제거
    if c == b[-1] and ''.join(result[-len(b):]) == b:
        for i in range(len(b)):
            result.pop()

print(''.join(result) if len(result) > 0 else 'FRULA')
