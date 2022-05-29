from collections import deque

# global
D = 4
DI = ((-1, -1, 0, 0), (-1, -1, 0, 0), (0, 0, 1, 1), (0, 0, 1, 1))
DJ = ((-1, 0, -1, 0), (0, 1, 0, 1), (-1, 0, -1, 0), (0, 1, 0, 1))
DELETED, ISTRACED = 'd', 1
TRACED = [[0]*(30+1) for _ in range(30+1)]

def solution(m, n, board):
    board = [deque(row) for row in zip(*board)]
    answer = 0
    
    while True:
        sub_answer = 0
        for i in range(n):
            for j in range(m):
                sub_answer += select(i, j, n, m, board)
        if not sub_answer: break
        
        answer += sub_answer
        delete(n, m, board)
        shift(n, m, board)
    return answer

def shift(n, m, board):
    for i in range(n):
        blank_block = 0
        for j in range(m):
            block = board[i].pop()
            if block == DELETED:
                blank_block += 1
            else:
                board[i].appendleft(block)
        for _ in range(blank_block):
            board[i].appendleft(DELETED)

def delete(n, m, board):
    for i in range(n):
        for j in range(m):
            if TRACED[i][j] == ISTRACED:
                board[i][j], TRACED[i][j] = DELETED, 0

def select(i, j, n, m, board):
    deleted = 0
    
    for d in range(D):
        can = True
        for c in range(D):
            ni, nj = i+DI[d][c], j+DJ[d][c]
            if ni == n or nj == m or ni == -1 or nj == -1:
                can = False; break;
            if board[i][j] == DELETED or board[ni][nj] != board[i][j]:
                can = False; break; 
        if can:
            for c in range(D):
                ni, nj = i+DI[d][c], j+DJ[d][c]
                deleted += [1, 0][TRACED[ni][nj] == ISTRACED]
                TRACED[ni][nj] = ISTRACED
    return deleted
