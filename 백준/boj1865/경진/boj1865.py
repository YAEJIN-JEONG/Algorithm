# https://www.acmicpc.net/problem/1865
# 웜홀
from sys import stdin


# 벨만 포드 알고리즘
# 한 정점에서 다른 모든 정점까지 최소 거리, 가중치 음수인 경우 사용
def bellmanford():
    global n, edges, answer
    # 기존 벨만 포드는 시작점을 첫 방문 한 뒤,
    # 이후 방문된 정점들의 간선 체크. (n - 1) 번 반복.
    # (벨만 포드의 경우 시작 점을 맨 처음 방문한다는 것과 (n - 1) 번 반복하는 것이 중요)

    # 이 문제에서는 시작점과 상관 없이 음의 싸이클이 존재하는지만 판단하면 됨 (시작점 x)
    distance = [inf] * (n + 1)

    for cnt in range(n + 1):
        for now, to, cost in edges:
            new_cost = distance[now] + cost
            if distance[to] > new_cost:
                distance[to] = new_cost
                # n 번째에 값이 갱신되는 경우 음의 싸이클 존재
                if cnt == n:
                    answer = 'YES'
                    return


if __name__ == '__main__':
    tc = int(stdin.readline())

    for _ in range(tc):
        n, m, w = map(int, stdin.readline().split())
        edges = []

        # 도로 입력, 양방향
        for _ in range(m):
            s, e, t = map(int, stdin.readline().split())
            edges.append((s, e, t))
            edges.append((e, s, t))
        # 웜홀 입력, 단방향
        for _ in range(w):
            s, e, t = map(int, stdin.readline().split())
            edges.append((s, e, -t))

        inf = 100000000
        answer = 'NO'
        # 벨만 포드
        bellmanford()

        print(answer)
