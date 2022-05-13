# https://programmers.co.kr/learn/courses/30/lessons/86052
def do_cycle(n, m, grid, visited, start):
    x, y, d = start
    # 위, 오른쪽, 아래, 왼쪽 순서
    # 방향 전환시 오른쪽: +1, 왼쪽: -1
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited[x][y][d] = True

    cnt = 0
    while True:
        x = (x + steps[d][0]) % n
        y = (y + steps[d][1]) % m
        cnt += 1

        if grid[x][y] == 'R':
            d = (d + 1) % len(steps)
        elif grid[x][y] == 'L':
            d = (d - 1) % len(steps)

        if visited[x][y][d]:
            return cnt if (x, y, d) == start else 0

        visited[x][y][d] = True


def solution(grid):
    n, m = len(grid), len(grid[0])
    # visited[x][y][d] -> (x, y) 에서 나가는 방향이 d
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    answer = []

    for x in range(n):
        for y in range(m):
            # d = (0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽)
            for d in range(4):
                if not visited[x][y][d]:
                    cnt = do_cycle(n, m, grid, visited, (x, y, d))
                    if cnt > 0:
                        answer.append(cnt)

    return sorted(answer)
