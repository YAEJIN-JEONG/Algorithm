# https://www.acmicpc.net/problem/2239
# 스도쿠
from sys import stdin

arr = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(9)]

# 0인 위치, n행 숫자들, n열 숫자들, 3 x 3 영역 숫자들
pos, n_row, n_col, n_square = [], [0] * 9, [0] * 9, [[0] * 3 for _ in range(3)]

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            pos.append([i, j])
        else:
            bit = 1 << arr[i][j]
            n_row[i] |= bit
            n_col[j] |= bit
            n_square[i // 3][j // 3] |= bit


# 백트래킹
def backtrack(index):
    if index == len(pos):
        for line in arr:
            print(''.join(map(str, line)))
        exit()
    else:
        # 현재 위치
        x, y = pos[index]
        # 가능하지 않은 숫자들
        not_available = n_row[x] | n_col[y] | n_square[x // 3][y // 3]

        for n in range(1, 10):
            mask = 1 << n
            unmask = ~mask
            if not not_available & mask:
                arr[x][y] = n
                n_row[x] |= mask
                n_col[y] |= mask
                n_square[x // 3][y // 3] |= mask
                backtrack(index + 1)
                n_square[x // 3][y // 3] &= unmask
                n_col[y] &= unmask
                n_row[x] &= unmask
                arr[x][y] = 0


backtrack(0)
