#특정 노드를 방문하고 연결된 모든 노드 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 아직 방문하지 않은 경우
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y]=1
        #상,하,좌,우 재귀 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m =map(int, input().split())

graph=[]
# n x m 그래프 입력 받기
for i in range(n):
    graph.append(list(map(int, input())))

#모든 위치에 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현 위치에서 dfs 수행
        if dfs(i,j) == True:
            result += 1

print(result)