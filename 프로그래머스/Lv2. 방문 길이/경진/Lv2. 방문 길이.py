# https://programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    # 방향
    moves = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
    # 위치, 방문한 길 집합
    x, y, visited = 0, 0, set()

    for d in dirs:
        nx, ny = x + moves[d][0], y + moves[d][1]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny

    return len(visited) // 2
