from itertools import permutations
from collections import deque

def solution(board, r, c):
    answer, GET, N = [256], 0, 4
    CARD_POSES = [[] for _ in range(7)]
    CARDS = set()
    DI, DJ = [-1,0,1,0], [0,1,0,-1]

    def cards_init():
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    CARD_POSES[board[i][j]].append((i,j))
                    CARDS.add(board[i][j])

    def bfs(i, j, i1, j1):
        if i == i1 and j == j1:
            return 0
        Q = deque()
        traced, traced[i][j] = [[0]*N for _ in range(N)], 1

        dist = 1
        Q.append((i, j))

        while Q:    
            for _ in range(len(Q)):
                i, j = Q.popleft()                

                for n in range(N):
                    ni, nj = i+DI[n], j+DJ[n]
                    if ni == -1 or ni == N or nj == -1 or nj == N:
                        continue
                    if traced[ni][nj]:
                        continue
                    if ni == i1 and nj == j1:
                        return dist
                    traced[ni][nj] = 1
                    Q.append((ni, nj))

                for n in range(N):
                    di, dj = DI[n], DJ[n]
                    ni, nj = i+di, j+dj

                    while ni >= 0 and ni < N and nj >= 0 and nj < N:
                        if board[ni][nj] > 0:
                            break
                        ci, cj = ni+di, nj+dj
                        if ci == -1 or ci == N or cj == -1 or cj == N:
                            break
                        ni, nj = ci, cj

                    if ni == -1 or ni == N or nj == -1 or nj == N:
                        continue
                    if traced[ni][nj]:
                        continue
                    if ni == i1 and nj == j1:
                        return dist

                    traced[ni][nj] = 1
                    Q.append((ni, nj))
            dist += 1

    def dfs(case, case_i, i, j, opened, ans):
        if case_i == len(CARDS):
            answer[GET] = min(answer[GET], ans)
            return
        if ans >= answer[GET]:
            return

        card = case[case_i]
        ni0, nj0 = CARD_POSES[card][0]
        ni1, nj1 = CARD_POSES[card][1]

        if opened == -1:
            dist0, dist1 = bfs(i, j, ni0, nj0), bfs(i, j, ni1, nj1)
            dfs(case, case_i, ni0, nj0, 0, ans+dist0)
            dfs(case, case_i, ni1, nj1, 1, ans+dist1)
        elif opened == 0:
            dist = bfs(i, j, ni1, nj1)
            board[ni0][nj0] = board[ni1][nj1] = 0
            dfs(case, case_i+1, ni1, nj1, -1, ans+dist+2)
            board[ni0][nj0] = board[ni1][nj1] = card
        else:
            dist = bfs(i, j, ni0, nj0)
            board[ni0][nj0] = board[ni1][nj1] = 0
            dfs(case, case_i+1, ni0, nj0, -1, ans+dist+2)
            board[ni0][nj0] = board[ni1][nj1] = card

    def call():
        for case in permutations(CARDS):
            dfs(case, 0, r, c, -1, 0)
        return answer[GET]

    cards_init()
    return call()
