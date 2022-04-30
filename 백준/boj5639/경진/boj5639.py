# https://www.acmicpc.net/problem/5639
# 이진 검색 트리
from sys import stdin, setrecursionlimit


def postorder(start, end):
    global preorder

    if start > end:
        return

    root = preorder[start]

    # left 서브 트리 노드 개수 세기
    left_cnt = 0
    for i in range(start, end + 1):
        if preorder[i] > root:
            break
        left_cnt += 1
    left_cnt -= 1

    # left, right subtree
    postorder(start + 1, start + left_cnt)
    postorder(start + left_cnt + 1, end)
    print(root)


if __name__ == '__main__':
    # pre:  root -> left -> right
    # post: left -> right -> root
    preorder = []
    while True:
        s = stdin.readline().rstrip()
        if len(s) == 0:
            break
        preorder.append(int(s))

    # recursion 제한 변경
    setrecursionlimit(10 ** 6)
    postorder(0, len(preorder) - 1)
