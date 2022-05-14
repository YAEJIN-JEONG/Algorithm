# https://programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque


def bfs(place, x, y, visited):
    deq = deque([(x, y, 0)])
    visited[x][y] = True

    while deq:
        x, y, d = deq.popleft()

        # 0 < 거리 <= 2 일 때, 해당 위치가 응시자 인지 검사
        if 0 < d <= 2 and place[x][y] == 'P':
            return False
        if d > 2:
            continue

        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] != 'X' and not visited[nx][ny]:
                deq.append((nx, ny, d + 1))
                visited[nx][ny] = True

    return True


def solution(places):
    answer = []
    for place in places:
        for x in range(5):
            for y in range(5):
                visited = [[False] * 5 for _ in range(5)]
                # 응시자가 있는 곳에서 bfs
                if place[x][y] == 'P':
                    # 거리 안지키고 있으면 0 추가 후 다음 장소로 넘어가기
                    if not bfs(place, x, y, visited):
                        answer.append(0)
                        break
            else:
                continue
            break
        else:
            # 거리 잘 지키고 있으면 1 추가
            answer.append(1)

    return answer
