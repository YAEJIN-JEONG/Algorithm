import sys
#n,m
n,m = map(int,sys.stdin.readline().strip().split())

#듣도 못한 사람,보도 못한 사람을 입력 받음
nonLisen=[sys.stdin.readline().strip() for i in range(n)]
nonWatch=[sys.stdin.readline().strip() for i in range(m)]

#set 함수 intersection(교집합)사용 O(len(s)+len(t))
li = list(set(nonWatch).intersection(set(nonLisen)))
#결과 정렬
li.sort()

#출력
print(len(li))
for i in li:
    print(i)