INF = int(1e9)

# 노드, 간선 입력
n = int(input())
m = int(input())
# 2차원 리스트 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용 c
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
# k 거처가는 노드, a 출발 노드, b 도착 노드
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 무한
        if graph[a][b] == INF :
            print("INFINITY",end="")
        else:
            print(graph[a][b],end="")
        print()