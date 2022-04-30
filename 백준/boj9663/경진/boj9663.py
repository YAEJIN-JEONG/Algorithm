# https://www.acmicpc.net/problem/9663
# N-Queen
from sys import stdin


def backtrack(row, cols):
    global n, answer

    # 모든 행에 퀸을 배치한 경우
    if row == n:
        answer += 1
    else:
        # i = 놓을 수 있는 열 후보
        for i in range(n):
            # 이미 같은 열에 놓인 퀸이 있으면 스킵
            if i in cols:
                continue
            # 대각선 방향에 놓인 퀸이 있으면 스킵
            for j in range(len(cols)):
                if abs(cols[j] - i) == row - j:
                    break
            # i 가 퀸을 놓을 수 있는 위치이면 퀸을 놓고 다음 행 진행
            else:
                cols.append(i)
                backtrack(row + 1, cols)
                cols.pop()


if __name__ == '__main__':
    n = int(stdin.readline())

    # 인덱스: row, 원소: col
    columns = []
    answer = 0

    backtrack(0, columns)

    print(answer)
