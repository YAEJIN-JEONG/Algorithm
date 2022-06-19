t=int(input())  #테스트 케이스 입력

for testCase in range(t):

    #노드의 수
    n= int(input())

    #모든 노드는 일대일로 연결되어 있다는 점에서
    # 리스트 하나로 관리 가능하다
    li = [0 for i in range(n+1)]

    for i in range(n-1):
        a,b = map(int, input().split())
        #바텀업 방식으로 찾아가기 떄문에 자직노드 인덱스에 부모노드 번호 할당
        li[b]=a

    #찾아야 할 노드
    a, b = map(int, input().split())
    ap = [a]
    bp = [b]

    # 단말노드부터 루트노드까지 탐색
    while li[a]:
        ap.append(li[a])
        a=li[a]
    while li[b]:
        bp.append(li[b])
        b=li[b]

    ap.reverse()
    bp.reverse()
    ap.append(-1)
    bp.append(-1)
    count = 0
    print(ap)
    print(bp)

    # 노드의 값이 달라지는 지점을 찾아서 그 인덱스를 반환
    while True:
        if ap[count] != bp[count] or ap[count]==bp[count]==-1:
            print(ap[count - 1])
            break
        else:
            count+=1