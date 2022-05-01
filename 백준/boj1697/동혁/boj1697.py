import sys
from collections import deque

#덱에 첫번쨰 원소를 꺼내서 -1,+1,*2한 결과를 덱에 넣는다
#덱에 포함할때 0이상 10만 미만이고, 기존에 dist에 있지 않은 값이어야 한다
#만들고자 하는값(k)이 덱 맨앞에 있다면 dist에서 연산 횟수를 찾아서 반환
def bfs():
    q = deque()
    q.append(n)

    #덱에 원소가 있는동안 반복
    while q:
        a=q.popleft()
        if a == k:
            print(dist[a])
            break
        for j in (a - 1, a + 1, a * 2):
            if 0 <= j <= MAX and not dist[j]:
                dist[j] = dist[a] + 1
                q.append(j)

#최대값
MAX = 100000
#해당하는 숫자가 몇번째 연산에서 나왔는지 담는 리스트
dist = [0] * (MAX + 1)
#n,k
n,k = map(int,sys.stdin.readline().strip().split())
bfs()