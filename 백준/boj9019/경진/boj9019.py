# https://www.acmicpc.net/problem/9019
# DSLR
# python3 으로 채점하면 시간초과, Pypy3 로 채점했음
# 같은 로직으로 다른 언어 사용 시 통과
from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    a, b = map(int, stdin.readline().split())

    deq = deque()
    # 이미 거쳐간 숫자인지 저장
    visited = set()
    deq.append((a, ''))
    visited.add(a)

    # bfs
    while deq:
        n, commands = deq.popleft()

        # 최종 숫자에 도달했으면 명령어 출력
        if n == b:
            print(commands)
            break
        
        # DSLR 배열 (값, 명령어) 튜플
        dslr = [
            ((n * 2) % 10000, 'D'),                 # D
            (9999 if n - 1 < 0 else n - 1, 'S'),    # S
            (n % 1000 * 10 + n // 1000, 'L'),       # L
            (n // 10 + n % 10 * 1000, 'R')          # R
        ]

        for i, c in dslr:
            # visited 에 없는 숫자만 처리
            if i not in visited:
                deq.append((i, commands + c))
                visited.add(i)
