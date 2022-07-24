# https://www.acmicpc.net/problem/1013
# Contact
from sys import stdin
import re

t = int(stdin.readline())

for _ in range(t):
    s = stdin.readline().rstrip()
    # 정규 표현식
    print('YES' if re.compile('(100+1+|01)+').fullmatch(s) else 'NO')
