import sys

def solution(N, G):
    SLASH, BACKSLASH, TYPE = [0]*(2*N+1), [0]*(2*N+1), 2
    answer = [0]*TYPE
    datas = [[] for _ in range(TYPE)]
    
    def init():
        for i in range(N):
            for j in range(N):
                if G[i][j]:
                    datas[(i+j)%2].append((i, j))
        
    def dfs(start, ans, type):
        answer[type] = max(answer[type], ans)

        for s in range(start+1, len(datas[type])):
            ni, nj = datas[type][s]
            nslash, nbackslash = ni+nj, ni-nj+N

            if SLASH[nslash] or BACKSLASH[nbackslash]:
                continue  
            SLASH[nslash] = BACKSLASH[nbackslash] = 1
            dfs(s, ans+1, type)
            SLASH[nslash] = BACKSLASH[nbackslash] = 0

    def call():
        init()
        for type in range(TYPE):
            dfs(-1, 0, type)
        return sum(answer)

    return call()

# driver
input = sys.stdin.readline
N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, G))
