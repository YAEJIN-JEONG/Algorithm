# https://programmers.co.kr/learn/courses/30/lessons/77485
def rotate(arr, x1, y1, x2, y2):
    x, y = x1, y1
    prev = arr[x1][y1]
    min_value = prev

    # 시계 방향 순서대로
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for step in steps:
        while True:
            nx = x + step[0]
            ny = y + step[1]

            if x1 <= nx <= x2 and y1 <= ny <= y2:
                arr[nx][ny], prev = prev, arr[nx][ny]
                x, y = nx, ny
                min_value = min(min_value, prev)
            else:
                break

    return min_value


def solution(rows, columns, queries):
    arr = [[i + (columns * j) for i in range(1, columns + 1)] for j in range(rows)]

    answer = []
    for x1, y1, x2, y2 in queries:
        # 테두리 회전
        answer.append(rotate(arr, x1 - 1, y1 - 1, x2 - 1, y2 - 1))

    return answer
