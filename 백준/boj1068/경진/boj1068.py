# https://www.acmicpc.net/problem/1068
# 트리
from sys import stdin


def dfs(node):
    global d, leaf, children

    if node == -1 or node == d:
        return

    # 자식이 없으면 리프 노드, 하나 있는 자식이 삭제될 노드이면 리프 노드
    if len(children[node]) == 0 or (len(children[node]) == 1 and children[node][0] == d):
        leaf += 1

    for edge in children[node]:
        dfs(edge)


if __name__ == '__main__':
    n = int(stdin.readline())
    parents = list(map(int, stdin.readline().split()))
    # index = parent, 원소 = child
    children = [[] for _ in range(n)]
    root = 0
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)

    d = int(stdin.readline())
    leaf = 0

    dfs(root)
    print(leaf)
