# https://www.acmicpc.net/problem/1918
# 후위 표기식
from sys import stdin
from collections import deque

s = stdin.readline()
answer = ''

deq = deque()
for c in s:
    # 피연산자는 그냥 출력
    if c.isalpha():
        answer += c
    # 여는 괄호면 스택에 입력
    elif c == '(':
        deq.append(c)
    # 닫는 괄호면 여는 괄호 만날 때 까지 모든 연산자 출력
    elif c == ')':
        while deq and deq[-1] != '(':
            answer += deq.pop()
        deq.pop()
    # 곱하기나 나누기는 우선순위가 같은, 먼저 들어온 곱하기와 나누기 출력
    elif c == '*' or c == '/':
        while deq and (deq[-1] == '*' or deq[-1] == '/'):
            answer += deq.pop()
        deq.append(c)
    # 더하기와 빼기는 우선순위가 가장 낮음.
    # 괄호 안이 아니면 먼저 들어온 연산자 모두 출력
    elif c == '+' or c == '-':
        while deq and deq[-1] != '(':
            answer += deq.pop()
        deq.append(c)

# 남은 연산자 모두 출력
while deq:
    answer += deq.pop()

print(answer)
