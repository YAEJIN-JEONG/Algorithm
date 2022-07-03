import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
approach = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            c = arr[i] + arr[j] + arr[k]
            if c <= m:
                if m - approach > m - c:
                    approach = c
print(approach)