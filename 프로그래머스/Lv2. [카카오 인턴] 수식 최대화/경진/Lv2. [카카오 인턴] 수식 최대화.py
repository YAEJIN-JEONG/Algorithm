# https://programmers.co.kr/learn/courses/30/lessons/67257
from collections import deque
import itertools
import re


# 중위 표기식 -> 후위 표기식
def to_post_exp(exp, priority):
    post_exp, operators = [], deque()

    for now in exp:
        # 숫자면 리스트에 추가
        if now.isnumeric():
            post_exp.append(int(now))
        else:
            # 현재 연산자 보다 우선순위 높은 연산자 나올 때 까지 스택에서 다 꺼냄
            while operators and priority[operators[-1]] <= priority[now]:
                post_exp.append(operators.pop())
            # 현재 연산자 스택에 추가
            operators.append(now)

    # 남은 연산자 리스트에 추가
    while operators:
        post_exp.append(operators.pop())

    return post_exp


# 후위 표기식 계산
def calc(exp):
    stack = deque()

    for now in exp:
        # 숫자면 스택에 넣기
        if type(now) == int:
            stack.append(int(now))
        else:
            # 연산자면 스택에서 숫자 두개 꺼내서 계산 후 다시 스택에 넣기
            a, b = stack.pop(), stack.pop()

            if now == '+':
                stack.append(a + b)
            elif now == '-':
                stack.append(b - a)
            else:
                stack.append(a * b)

    return stack[0]


def solution(expression):
    exp = re.split('([+\\-*])', expression)
    # 우선 순위 경우의 수
    priorities = itertools.permutations([0, 1, 2])

    answer = 0
    for a, b, c in priorities:
        # 우선 순위
        priority = {'+': a, '-': b, '*': c}
        # 후위 표기식 변환
        post_exp = to_post_exp(exp, priority)
        # 후위 표기식 계산
        answer = max(answer, abs(calc(post_exp)))

    return answer
