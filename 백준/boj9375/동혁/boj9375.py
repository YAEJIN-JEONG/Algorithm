import sys
from collections import *

#테스트 케이스
t = int(sys.stdin.readline().strip())
#유사 딕셔너리(append 지원)
li = defaultdict(list)

for i in range(t):
    a=int(sys.stdin.readline().strip())
    for j in range(a):
        item,category = map(str, sys.stdin.readline().strip().split())
        #키에는 의상 종류를, 밸류에는 리스트로 물건들 관리
        li[category].append(item)

#(의상 종류의 개수 + 1) * (의상 종류의 개수 + 1) ...-1
    sum=1
    for j in li:
        sum*=len(li[j])+1
    print(sum-1)
    #배열 초기화
    li.clear()