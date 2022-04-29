from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복
    while queue :
        x,y = queue.popleft()
        #현 위치에서 4가지 방향으로 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 공간 벗어난 경우 무시
            if nx < 0 or nx >=n or ny < 0 or ny >=m:
                continue
            #벽인 경우
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    #마지막 노드까지 최단 거리 반환
    return graph[n-1][m-1]

n,m = map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))
