# https://www.acmicpc.net/problem/17219
# 비밀번호 찾기
from sys import stdin

n, m = map(int, stdin.readline().split())

password = {}
for _ in range(n):
    k, v = stdin.readline().rstrip().split()
    password[k] = v

for _ in range(m):
    s = stdin.readline().rstrip()
    print(password[s])
