# https://www.acmicpc.net/problem/14939
# 불 끄기
from sys import stdin
import copy


# 스위치 누르기
def press(target, x, y):
    steps = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    for step in steps:
        nx = x + step[0]
        ny = y + step[1]

        if 0 <= nx < 10 and 0 <= ny < 10:
            target[nx][ny] ^= 1


if __name__ == '__main__':
    state = [[0] * 10 for _ in range(10)]

    # 전구 꺼진 곳 0, 켜진 곳 1
    for i in range(10):
        s = stdin.readline().rstrip()
        for j in range(10):
            if s[j] == 'O':
                state[i][j] = 1

    # 첫 행을 기준으로 스위치를 누르는 모든 경우 카운트
    press_cnt = [101] * (1 << 10)

    for i in range(1 << 10):
        # 원본 배열 복사
        n_state = copy.deepcopy(state)
        cnt = 0

        # 첫 행에서 스위치를 누르는 경우에 누르기
        for j in range(10):
            if i & (1 << j) != 0:
                press(n_state, 0, j)
                cnt += 1

        # 2행 부터 바로 위에 전구가 켜져있으면 스위치 누르기
        for r in range(1, 10):
            for c in range(10):
                if n_state[r - 1][c] == 1:
                    press(n_state, r, c)
                    cnt += 1

        # 위 작업 완료 후, 맨 아랫줄에 전구가 다 꺼져있으면 성공
        if sum(n_state[9]) == 0:
            press_cnt[i] = cnt

    min_cnt = min(press_cnt)
    print(min_cnt if min_cnt < 101 else -1)
