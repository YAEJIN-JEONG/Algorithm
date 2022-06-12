# https://www.acmicpc.net/problem/1799
# 비숍
from sys import stdin

n = int(stdin.readline())
board = [list(stdin.readline().rstrip().split()) for _ in range(n)]

# 비숍을 놓을 수 있는 위치 (흑, 백 나누어 입력)
candidates = [[] for _ in range(2)]
for i in range(n):
    for j in range(n):
        if board[i][j] == '1':
            candidates[(i + j) % 2].append([i, j])

# 흑, 백 칸에 각각 놓는 비숍 개수
answer = [0, 0]


# 백트래킹
def backtrack(start, depth, selected, k):
    global n, candidates, answer

    # 최대값 갱신이 불가능한 경우
    if answer[k] == len(candidates[k]) or depth + (len(candidates[k]) - start) <= answer[k]:
        return

    answer[k] = max(answer[k], depth)

    # 가능한 좌표에 대해 dfs
    for idx in range(start, len(candidates[k])):
        x, y = candidates[k][idx][0], candidates[k][idx][1]

        if is_valid(x, y, selected):
            selected.add((x, y))
            backtrack(idx + 1, depth + 1, selected, k)
            selected.remove((x, y))


# 비숍을 놓을 수 있는 위치인지 확인
def is_valid(x, y, selected):
    global n
    moves = [[-1, -1], [-1, 1]]

    for move in moves:
        for k in range(1, x + 1):
            nx, ny = x + move[0] * k, y + move[1] * k
            if nx < 0 or ny >= n:
                break
            if (nx, ny) in selected:
                return False

    return True


# 흑, 백 각각 백트래킹
for i in range(2):
    backtrack(0, 0, set(), i)

print(sum(answer))
