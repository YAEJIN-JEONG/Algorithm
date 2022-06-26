import sys
from collections import deque
queue = deque()
li = []
n,k = map(int, sys.stdin.readline().split())

for i in range(1,n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    li.append(queue.popleft())

print('<',end='')
for i in range(len(li)-1):
    print(li[i],end=', ')
print(li[-1],end='')
print('>')