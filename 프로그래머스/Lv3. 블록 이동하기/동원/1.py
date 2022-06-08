from collections import deque

def solution(board):
    N, D, MAX_ANS, BLOCK = len(board), 4, 10000, 1
    DX, DY = (-1, 0, 1, 0), (0, 1, 0, -1)
    Directions = {(1,0): 0, (0,-1): 1, (-1,0): 2, (0,1): 3}
    traced = [[[MAX_ANS]*D for _ in range(N)] for _ in range(N)]
    Q = deque()
    
    def can_move(x, y):
        if x == -1 or x == N or y == -1 or y == N:
            return False
        return board[x][y] != BLOCK
    
    # 평행이동
    def normal_move(x1, y1, x2, y2, dist):
        for d in range(D):
            nx1, ny1, nx2, ny2 = x1+DX[d], y1+DY[d], x2+DX[d], y2+DY[d]
            if not (can_move(nx1, ny1) and can_move(nx2, ny2)):
                continue
                    
            n1d = Directions[(nx1-nx2, ny1-ny2)]
            n2d = Directions[(nx2-nx1, ny2-ny1)]

            if traced[nx1][ny1][n1d] != MAX_ANS: continue
            traced[nx1][ny1][n1d] = traced[nx2][ny2][n2d] = dist
            Q.appendleft((nx1, ny1, nx2, ny2))
            
    # 회전이동
    def rotate_move(rx, ry, cx, cy, dist):
        bx, by = cx-rx, cy-ry
        nxy = ((by+rx, bx+ry), ((-1)*by+rx, (-1)*bx+ry))

        for nx, ny in nxy:
            if not can_move(nx, ny): continue
            
            block_x = nx if nx != rx else cx
            block_y = cy if ny == ry else ny
            if board[block_x][block_y] == BLOCK: continue
            
            nd = Directions[(nx-rx, ny-ry)]
            rd = Directions[(rx-nx, ry-ny)]
                        
            if traced[nx][ny][nd] != MAX_ANS: continue
            traced[nx][ny][nd] = traced[rx][ry][rd] = dist
            Q.appendleft((nx, ny, rx, ry))

    def bfs():
        dist = 1
        Q.appendleft((0, 0, 0, 1))
        traced[0][0][1] = traced[0][1][3] = 0
        
        while Q:
            for _ in range(len(Q)):
                x1, y1, x2, y2 = Q.pop()
                normal_move(x1, y1, x2, y2, dist)
                rotate_move(x1, y1, x2, y2, dist)
                rotate_move(x2, y2, x1, y1, dist)
            dist += 1
    
    # driver
    bfs()
    return min(traced[-1][-1])