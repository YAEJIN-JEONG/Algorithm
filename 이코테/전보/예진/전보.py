import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
# 노드, 간선, 시작 노드 입력
n,m,start = map(int, input().split())
# 각 노드에 연결되어 있는 노드 정보 담는 리스트
graph = [[]for i in range(n+1)]
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력
for _ in range(m):
    x,y,z=map(int,input().split())
    # x -> y 비용 z
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance,d)
print(count-1,max_distance)
