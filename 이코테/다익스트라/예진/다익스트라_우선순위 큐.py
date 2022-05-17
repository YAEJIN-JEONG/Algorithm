import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 개수 입력
n,m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드에 연결되어 있는 노드의 정보를 담는 리스트 초기화
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    # a 번 노드에서 b 번 노드로 가는 비용이 c
    graph[a].append((b,c))

def dijktra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start]=0
    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now =heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijktra(start)

for i in range(1,n+1):
    if distance[i] ==INF:
        print("INFINITY")
    else:
        print(distance[i])
