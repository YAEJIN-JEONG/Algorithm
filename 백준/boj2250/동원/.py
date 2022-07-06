import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N = int(input())
    G = [None]+sorted(list(map(int, input().split())) for _ in range(N))
    P = [n for n in range(N+1)]
    idx = [0] * (N+1)
    now_idx, GET = [0], 0

    def root():
        node = 1
        while P[node] != node:
            node = P[node]
        return node  

    def parent():
        for me, left, right in G[1:]:
            if left != -1: P[left] = me
            if right != -1: P[right] = me

    def indexing(node):
        if node == -1: return
        me, left, right = G[node]
        indexing(left)
        idx[node] = now_idx[GET]
        now_idx[GET] += 1
        indexing(right)

    def bfs(root):
        level, cur_level, width = 1, 0, 1
        q = deque()
        
        q.append(root)
        while q:
            cur_level += 1
            cur_width = idx[q[-1]] - idx[q[0]] + 1
            if cur_width > width:
                level, width = cur_level, cur_width
            for _ in range(len(q)):
                _, left, right = G[q.popleft()]
                if left != -1: q.append(left)
                if right != -1: q.append(right)
        print(str(level) + " " + str(width))     

    #driver
    parent()
    r = root()
    indexing(r)
    bfs(r)
    
solution()
