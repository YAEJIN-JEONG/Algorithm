import sys
input = sys.stdin.readline
# 무한 의미 : 10억 설정
INF = int(1e9)

# 노드와 간선의 개수 입력
n,m = map(int,input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 초기화
graph = [[] for i in range(n+1)]
# 방문 여부 확인하는 리스트 초기화
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    # 최단 거리가 가장 짧은 노드의 인덱스
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화, 출발노드 방문처리, 출발노드까지의 거리 0으로 설정
    distance[start] = 0
    visited[start]= True
    # 출발노드로 부터 당장 도달가능한 다른 노드까지의 거리 갱신
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작노드를 제외한 n-1개의 노드에 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now]=True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] ==INF:
        print("INFINITY")
    else:
        print(distance[i])