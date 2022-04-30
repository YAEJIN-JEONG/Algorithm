# https://www.acmicpc.net/problem/5525
from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline()
# 문자열 인덱스, 정답 카운트, 패턴을 만족하면서 연속된 O 개수 카운트
index, cnt, o_count = 2, 0, 0
while index < len(s):
    if s[index] == 'I' and s[index-1] == 'O' and s[index-2] == 'I':
        o_count += 1
        index += 1
    else:
        o_count = 0

    if o_count >= n:
        cnt += 1

    index += 1

print(cnt)
