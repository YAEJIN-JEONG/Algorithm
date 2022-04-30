# https://www.acmicpc.net/problem/2263
# 트리의 순회
from sys import stdin, setrecursionlimit


def preorder(in_start, in_end, post_start, post_end):
    global inorder, postorder, idx_inorder
    # 재귀 종료
    if in_start > in_end or post_start > post_end:
        return

    # 트리의 루트 노드는 postorder 마지막 노드
    root = postorder[post_end]
    print(root, end=' ')

    # inorder 에서 root 의 위치
    idx_inorder_root = idx_inorder[root]

    # inorder 의 root 기준 (왼쪽, 오른쪽) 은 (왼쪽, 오른쪽) 트리
    # 왼쪽, 오른쪽 트리 노드 개수
    left_cnt = idx_inorder_root - in_start
    right_cnt = in_end - idx_inorder_root

    # inorder => (left, root, right)
    # postorder => (left, right, root)
    # left
    preorder(in_start, in_start + left_cnt - 1, post_start, post_start + left_cnt - 1)
    # right
    preorder(in_end - right_cnt + 1, in_end, post_end - right_cnt, post_end - 1)


if __name__ == '__main__':
    n = int(stdin.readline())
    inorder = list(map(int, stdin.readline().split()))
    postorder = list(map(int, stdin.readline().split()))

    idx_inorder = [0] * (n + 1)
    for index, i in enumerate(inorder):
        idx_inorder[i] = index

    # recursion limit 변경 (파이썬은 기본 재귀 스택 1000번 넘으면 오류)
    setrecursionlimit(10 ** 6)
    preorder(0, n - 1, 0, n - 1)
