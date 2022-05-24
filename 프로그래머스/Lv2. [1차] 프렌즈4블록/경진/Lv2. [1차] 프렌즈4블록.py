# https://programmers.co.kr/learn/courses/30/lessons/17679
# 게임 진행
def process(m, n, board):
    # 터뜨릴 타겟
    target = set()

    for x in range(m):
        for y in range(n):
            now = board[x][y]
            if now == '':
                continue
            # 2x2 블록이 같은 모양인지 확인
            temp = {(x, y)}
            for nx, ny in ((x, y + 1), (x + 1, y), (x + 1, y + 1)):
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == now:
                    temp.add((nx, ny))
                else:
                    break
            else:
                # 2x2 블록이 같은 모양이면 터뜨릴 타겟에 추가
                target |= temp
    # 타겟 터뜨리기
    for x, y in target:
        board[x][y] = ''

    # 터진 공간 채우기
    down(m, n, board)

    return len(target)


# 터진 공간 채우기
def down(m, n, board):
    for x in range(m - 1, -1, -1):
        for y in range(n):
            if board[x][y] == '':
                temp = ''
                for nx in range(x, -1, -1):
                    if board[nx][y] != '':
                        temp, board[nx][y] = board[nx][y], temp
                        break
                else:
                    continue
                board[x][y] = temp


def solution(m, n, board):
    board = list(map(list, board))

    answer = 0
    while True:
        cnt = process(m, n, board)
        # 더 이상 터뜨릴 블록이 없으면 스톱
        if cnt == 0:
            break
        answer += cnt

    return answer
