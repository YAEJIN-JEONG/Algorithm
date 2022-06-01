#global
Answer = 169
Max_nodes = 0
D = 4
DI, DJ = [-1, 0, 1, 0], [0, 1, 0, -1]
 
def service(n, graph):
    nodes = get_nodes(n, graph)
    check(n, graph, nodes, 0, 0, 0)
    return [Answer, 0][Max_nodes == 0]
 
def check(n, graph, nodes, wired, start, answer):
    global Answer, Max_nodes
    if start == len(nodes):
        if wired > Max_nodes:
            Max_nodes = max(wired, Max_nodes)
            Answer = answer
        elif wired == Max_nodes:
            Answer = min(Answer, answer)
        return
 
    possible_nodes = wired+(len(nodes)-start)
    if possible_nodes < Max_nodes:
        return
    if possible_nodes == Max_nodes and answer+(len(nodes)-start) >= Answer:
        return
 
    node = nodes[start]
    for d in range(D):
        bi, bj = border(n, graph, node, d)
        if graph[bi][bj]: continue
        if can_wired(n, graph, node, d):
            wire = abs(bi-node[0]) + abs(bj-node[1])
            wirling(n, graph, node, d)
            check(n, graph, nodes, wired+1, start+1, answer+wire)
            wirling(n, graph, node, d)
    check(n, graph, nodes, wired, start+1, answer)
 
def wirling(n, graph, node, d):
    i, j = node
    di, dj = DI[d], DJ[d]
 
    while not (i==0 or i==n-1 or j==0 or j==n-1):
        i, j = i+di, j+dj
        graph[i][j] = [1, 0][graph[i][j]]
     
def border(n, graph, node, d):
    i, j = node
    if d == 0: return (0, j)
    elif d == 1: return (i, n-1)
    elif d == 2: return (n-1, j)
    else: return (i, 0)
     
def can_wired(n, graph, node, d):
    i, j = node
    di, dj = DI[d], DJ[d]
 
    while not (i==0 or i==n-1 or j==0 or j==n-1):
        i, j = i+di, j+dj
        if graph[i][j]: return False
    return True
 
def get_nodes(n, graph):
    nodes = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if graph[i][j] == 1:
              nodes.append((i, j))
    return nodes
 
 
#import sys
 
 
'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
 
      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.
 
      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case} {service(N, G)}')
    Answer = 169
    Max_nodes = 0
    # ///////////////////////////////////////////////////////////////////////////////////
