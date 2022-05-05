#https://ralp0217.tistory.com/entry/Python3-%EC%99%80-PyPy3-%EC%B0%A8%EC%9D%B4
import sys

#pypy3 사용시 메모리 초과(위 주소 참조)
#set으로 중복 관리, remove 사용시 없는 값에 대해 에러 발생 discard로 대체 사용
n = int(sys.stdin.readline().rstrip())
li = set()

for i in range(n):
    a = sys.stdin.readline().strip().split()

    #문자가 하나만 들어올 시
    if len(a)==1:
        if a[0] == 'all':
            li = set([i for i in range(1,21)])
        else:
            li = set()
    #문자가 2개 들어올 시
    else:
        num = int(a[1])
        if a[0] == 'add':
            li.add(num)
        elif a[0] == 'remove':
            li.discard(num)
        elif a[0] == 'check':
            if num in li:
                print(1)
            else:
                print(0)
        elif a[0] == 'toggle':
            if num in li:
                li.discard(num)
            else:
                li.add(num)