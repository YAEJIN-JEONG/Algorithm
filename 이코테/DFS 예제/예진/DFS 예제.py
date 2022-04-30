def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


#각 노드가 연결된 정보를 표현 (2차원 리스트)
#노드는 주로 1번부터 시작되므로 0번은 비워두기
graph = [
    [],
    [2, 3, 8], #1번 노드 인접
    [1, 7], #2번 노드 인접
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
#index 0 은 사용하지 않으므로 하나 더 큰 크기인 9로 선언
#각 노드에서 1을 뺀 값으로 처리하는 것보다
#index 0을 사용하지 않는 방식이 노드의 번호를 인덱스 형태로 매핑할 수 있어 직관적
visited = [False] * 9

dfs(graph, 1, visited)