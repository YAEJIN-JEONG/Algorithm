# https://www.acmicpc.net/problem/14500
# 테트로미노
from sys import stdin


def dfs(x, y, score, depth):
    global n, m, paper, answer, max_value
    # depth 가 3 이면 블록 4개 선택 완료
    if depth == 3:
        answer = max(answer, score)
    # 현재까지 나온 정답보다 더 큰 수가 나올 수 없는 상태일 때 진행하지 않기
    elif answer < score + (3 - depth) * max_value:
        # 다음 블록 선택 방향
        steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for step in steps:
            nx = x + step[0]
            ny = y + step[1]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 'ㅗ' 모양 제외한 모든 모양
                visited[nx][ny] = True
                dfs(nx, ny, score + paper[nx][ny], depth + 1)
                visited[nx][ny] = False
                # 'ㅗ' 모양 만들기, 세 개 선택한 상태에서 이전 좌표 넘겨 줌
                if depth == 1:
                    visited[nx][ny] = True
                    dfs(x, y, score + paper[nx][ny], depth + 1)
                    visited[nx][ny] = False


if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())
    paper = [[i for i in list(map(int, stdin.readline().split()))] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 점수 최대값
    max_value = max(map(max, paper))
    answer = 0

    # 모든 위치에서 가능한 테트로미노 만들기
    for r in range(n):
        for c in range(m):
            visited[r][c] = True
            dfs(r, c, paper[r][c], 0)
            visited[r][c] = False

    print(answer)
