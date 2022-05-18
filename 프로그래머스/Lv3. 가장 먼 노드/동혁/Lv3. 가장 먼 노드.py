def solution(n, edge):
    from collections import defaultdict

    #defulatdict를 사용하면 정렬하는 시간이 필요 없어짐
    li = defaultdict(list)

    #양방향으로 에지를 가짐
    for i in edge:
        li[i[0]].append(i[1])
        li[i[1]].append(i[0])

    search = [1]    #시작을 1에서 부터 시작함
    check=[0 for i in range(n+1)]   #간선이 몇개 존재하는지 관리하는 배열
    check[1]=1  #첫번째노드를 체크하지 못하게 설정

    for i in search:
        for j in li[i]:

            #탐색하지 않은 노드일 경우 직전 노드의 간선 + 1
            #j not in search로 했었을때 탐색 횟수가 너무 커져서 시간초과(최대 간선 수 50000)
            if check[j]==0:
                search.append(j)
                check[j] = check[i] + 1

    #간선수가 가장 많은 노드의 수를 구함
    return check.count(max(check))
