# https://www.acmicpc.net/problem/11723
# 집합
from sys import stdin

m = int(stdin.readline())
s = set()

for _ in range(m):
    command = stdin.readline().split()

    if len(command) == 1:
        if command[0] == 'all':
            s = {i for i in range(1, 21)}
        else:
            s.clear()
    else:
        c, i = command[0], int(command[1])

        if c == 'add':
            s.add(i)
        elif c == 'remove':
            s.discard(i)
        elif c == 'check':
            print(1 if i in s else 0)
        else:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
