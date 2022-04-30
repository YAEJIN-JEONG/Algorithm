# https://www.acmicpc.net/problem/1991
# 트리 순회
from sys import stdin


# 전위 순회
def preorder(p):
    global nodes
    print(p, end='')

    left_node, right_node = nodes[p]

    if left_node != '.':
        preorder(left_node)
    if right_node != '.':
        preorder(right_node)


# 중위 순회
def inorder(p):
    global nodes

    left_node, right_node = nodes[p]

    if left_node != '.':
        inorder(left_node)
    print(p, end='')
    if right_node != '.':
        inorder(right_node)


# 후위 순회
def postorder(p):
    global nodes

    left_node, right_node = nodes[p]

    if left_node != '.':
        postorder(left_node)
    if right_node != '.':
        postorder(right_node)
    print(p, end='')


if __name__ == '__main__':
    n = int(stdin.readline())
    # {노드: (왼쪽, 오른쪽), ...} 형태로 저장
    nodes = {}

    for _ in range(n):
        node, left, right = stdin.readline().rstrip().split()
        nodes[node] = (left, right)

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
