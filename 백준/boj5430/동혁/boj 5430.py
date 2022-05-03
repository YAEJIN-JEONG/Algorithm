import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for i in range(T):
    p = [i for i in sys.stdin.readline().strip()]
    n = int(sys.stdin.readline().strip())
    queue = deque(sys.stdin.readline().strip()[1:-1].split(','))

    rev= True
    flag = True
    if n == 0:
        queue = []


    for j in p:
        if j == 'R':
            rev = not rev
        elif j == 'D':
            if len(queue) < 1:
                flag = not flag
                print("error")
                break
            else:
                if rev:
                    queue.popleft()
                else:
                    queue.pop()
    if flag:
        if rev:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")