import sys
from collections import deque

#테스트 케이스
T = int(sys.stdin.readline().strip())

for i in range(T):
    #입력받기
    p = [i for i in sys.stdin.readline().strip()]
    n = int(sys.stdin.readline().strip())
    queue = deque(sys.stdin.readline().strip()[1:-1].split(','))

    rev= True   #결과출력 or error
    flag = True #True는 정방향 False는 역방향

    #갯수가 0일떄 배열 초기화
    if n == 0:
        queue = []


    for j in p:
        #R이 들어오면 방향을 바꿈
        if j == 'R':
            rev = not rev
        #아무것도 없는상태에서 D가 들어오면 종료
        elif j == 'D':
            if len(queue) < 1:
                flag = not flag
                print("error")
                break
            else:
                if rev:
                    queue.popleft()
                else:
                    queue.pop()

    #출력
    if flag:
        if rev:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")