# https://programmers.co.kr/learn/courses/30/lessons/87377
def solution(line):
    # 최대값 10^15
    min_x, min_y = 1000000000000000, 1000000000000000

    cross = []
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            if a * d - b * c == 0:
                continue
            x, y = (b * f - e * d) / (a * d - b * c), (e * c - a * f) / (a * d - b * c)
            if a * d - b * c != 0 and x.is_integer() and y.is_integer():
                x, y = int(x), int(y)
                cross.append([x, y])
                min_x, min_y = min(min_x, x), min(min_y, y)

    # 각 교점 위치 보정, 격자판 크기 정하기
    rows, cols = -1000000000000000, -1000000000000000
    for i in range(len(cross)):
        cross[i] = [cross[i][0] - min_x, cross[i][1] - min_y]
        rows, cols = max(rows, cross[i][1]), max(cols, cross[i][0])

    # 격자판
    answer = [['.'] * (cols + 1) for _ in range(rows + 1)]

    # 교점 격자판에 표시
    for x, y in cross:
        answer[rows - y][x] = '*'

    # 행 마다 문자열로 바꿔서 반환
    return list(map(lambda elem: ''.join(elem), answer))
