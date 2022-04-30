# https://www.acmicpc.net/problem/11047
# 동전 0
from sys import stdin

n, k = map(int, stdin.readline().split())

coins = [int(stdin.readline()) for _ in range(n)]

cnt = 0
# coins[n] 은 coins[n-1] 의 배수, 제일 비싼 동전부터 고르면 됨, 그리디
for i in range(n - 1, -1, -1):
    cnt += k // coins[i]
    k %= coins[i]

print(cnt)
