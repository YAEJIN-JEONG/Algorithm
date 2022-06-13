# https://www.acmicpc.net/problem/1987
# 알파벳
from sys import stdin

r, c = map(int, stdin.readline().split())
board = [list(map(lambda char: ord(char) - ord('A'), stdin.readline().rstrip())) for _ in range(r)]

promising = set()
promising.add((0, 0, 1, 1 << board[0][0]))
answer = 0

while promising:
    x, y, d, used = promising.pop()

    answer = max(answer, d)
    if answer == 26:
        break

    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for move in moves:
        nx, ny = x + move[0], y + move[1]

        if 0 <= nx < r and 0 <= ny < c and used & (1 << board[nx][ny]) == 0:
            promising.add((nx, ny, d + 1, used | (1 << board[nx][ny])))

print(answer)
