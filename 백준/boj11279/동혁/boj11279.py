import sys
import heapq

n=int(sys.stdin.readline().strip())
li=[]

#heapq를 사용 (최소 힙을 구현하는 모듈)
#-a 형태로 넣어서 보관하고 꺼낼때 다시 -를 해줘서 최대 큐로 사용
for i in range(n):
    a=int(sys.stdin.readline().strip())

    if a==0:
        if len(li)==0:
            print(0)
            continue
        b=heapq.heappop(li)
        print(-b)
        continue
    heapq.heappush(li,-a)