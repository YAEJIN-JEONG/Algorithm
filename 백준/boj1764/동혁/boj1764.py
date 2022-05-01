import sys
#n,m
n,m = map(int,sys.stdin.readline().strip().split())

nonLisen=[sys.stdin.readline().strip() for i in range(n)]
nonWatch=[sys.stdin.readline().strip() for i in range(m)]

#set에 교집합 함수 사용 및 리스트 정렬
li = list(set(nonWatch).intersection(set(nonLisen)))
li.sort()

print(len(li))
for i in li:
    print(i)