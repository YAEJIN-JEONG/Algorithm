from collections import deque

a,b = map(int,input().split())
q=deque([(a,1)])

def solve(a, b):
    q = deque([(a, 1)])

    while q:
        #(현제값,카운트)
        now, cnt = q.popleft()
        #값을 찾으면 출력
        if now == b:
            print(cnt)
            return

        #현제q가 조건에  부합하지않는다면 진행
        #2배,끝에 1추가(n*10+1)를 추가
        if now * 2 <= b:
            q.append((now * 2, cnt + 1))
        if now * 10 + 1 <= b:
            q.append((now * 10 + 1, cnt + 1))

    #끝까지 못찾는다면 -1
    print(-1)

solve(a, b)