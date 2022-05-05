import sys

n,m = map(int, sys.stdin.readline().strip().split())

#구간을 입력받고 메모이제이션(ex) li(n) = li(n-1) + a)
li = list(map(int,sys.stdin.readline().strip().split()))
dyLi=[0]
for i in range(n):
    dyLi.append(dyLi[i] + li[i])

#구간의 값을 구함 (ex) (1,2,3,4) - (1,2,3,4,5) = (4,5))
for i in range(m):
    a,b = map(int, sys.stdin.readline().strip().split())
    print(dyLi[b] - dyLi[a-1])