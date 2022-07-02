def solution():
    N, M, K = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]
    D, DN, GET, MAX_TIME = list(map(int, input().split())), 4, 0, 1000
    DI, DJ, OUT_OF_RANGE = [-1,1,0,0], [0,0,-1,1], {-1,N}
    P = [[list(map(int, input().split())) 
        for _ in range(DN)] for _ in range(M)]
    smell = [[[0, 0]]*N for _ in range(N)]
    removed = [0]

    def update_smell():
        for i in range(N):
            for j in range(N):
                if smell[i][j][1] > 0 :
                    smell[i][j][1] -= 1
                if g[i][j] != 0 :
                    smell[i][j] = [g[i][j], K]

    def move_fishes():
        ng = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N) :
                if g[i][j] != 0:
                    move_fish(ng, i, j)
        return ng

    # 모든 상어를 이동시키는 함수
    def move_fish(ng, i, j):
        fish, fish_idx = g[i][j], g[i][j]-1 
        direction, direction_idx = D[fish_idx], D[fish_idx]-1
        pi, pj, pd = None, None, None

        def death_or_live(ni, nj, nd):
            D[fish_idx] = nd
            if ng[ni][nj] == 0 :
                ng[ni][nj] = fish
            else:
                removed[GET] += 1
                ng[ni][nj] = min(ng[ni][nj], fish)

        for nd in P[fish_idx][direction_idx]:
            nd_idx = nd-1
            ni, nj = i + DI[nd_idx], j + DJ[nd_idx]
            if ni in OUT_OF_RANGE or nj in OUT_OF_RANGE:
                continue
            if smell[ni][nj][0] == fish and pi == None:
                pi, pj, pd = ni, nj, nd
            if smell[ni][nj][1] == 0:
                death_or_live(ni, nj, nd)
                return
        death_or_live(pi, pj, pd)

    def g_set(ng):
        for i in range(N):
            for j in range(N):
                g[i][j] = ng[i][j]

    def call():
        for time in range(1, MAX_TIME+1):
            update_smell() # 모든 위치의 냄새를 업데이트
            g_set(move_fishes())
            if removed[GET] == M-1: return time
        return -1
    print(call())

# driver
solution()
