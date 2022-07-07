import sys

def solution():
    input = sys.stdin.readline
    N, R, Q = map(int, input().split())
    E = [list(map(int, input().split())) for _ in range(N-1)]
    G, DB = [[] for _ in range(N+1)], [[] for _ in range(N+1)]
    QS = [int(input()) for _ in range(Q)]
    
    def graph():
        for i, j in E:
            G[i].append(j)
            G[j].append(i)

    def calculate(node):
        DB[node] = 1
        for new_node in G[node]:
            if not DB[new_node]:
                DB[node] += calculate(new_node)
        return DB[node]

    def answer():
        print('\n'.join(str(DB[q]) for q in QS))

    #driver
    graph()
    sys.setrecursionlimit(10**6)
    calculate(R)
    answer()
    
solution()
