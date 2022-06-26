import sys
n,k = map(int, sys.stdin.readline().strip().split())
li = list(map(int, sys.stdin.readline().strip().split()))
a=sorted(li, reverse=True)

print(a[:k][-1])