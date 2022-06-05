# https://programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    rows, cols, size = len(board), len(board[0]), 0
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    for x in range(rows):
        for y in range(cols):
            if board[x][y] == 1:
                # dp[x][y] = min(dp[x-1][y-1], dp[x-1][y], dp[x][y-1]) + 1
                dp[x + 1][y + 1] = min(dp[x][y], dp[x][y + 1], dp[x + 1][y]) + 1

            # 최대 크기 갱신
            size = max(size, dp[x + 1][y + 1])

    return size * size
