# https://www.acmicpc.net/problem/5430
from sys import stdin
from collections import deque

t = int(stdin.readline().rstrip())

for _ in range(t):
    # 입력 받기
    f = stdin.readline().strip()
    n = int(stdin.readline().strip())
    n_list = list(stdin.readline().strip()[1:-1].split(','))

    deq = deque(n_list) if n > 0 else deque()
    # n_order 홀수 -> reverse
    n_order = 0

    for c in f:
        if c == 'R':
            n_order += 1
        else:
            if not deq:
                print('error')
                break
            deq.popleft() if n_order % 2 == 0 else deq.pop()
    else:
        if n_order % 2 == 1:
            deq.reverse()
        print('[' + ','.join(deq) + ']')
