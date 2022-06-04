# https://programmers.co.kr/learn/courses/30/lessons/12952

# cols[i] 는 i번째 행에서 퀸의 위치
def backtrack(n, row, cols):
    if row == n:
        return 1

    cnt = 0
    for i in range(n):
        if is_valid(row, cols, i):
            cols[row] = i
            cnt += backtrack(n, row + 1, cols)

    return cnt


# col 에 놓을 수 있는지 판별
def is_valid(row, cols, col):
    for i in range(row):
        if cols[i] == col or abs(cols[i] - col) == abs(row - i):
            return False
    return True


def solution(n):
    return backtrack(n, 0, [0] * n)
