from collections import deque

def solution(n, edge):
    TRACED = [0] * (n+1)
    G = [[] for _ in range(n+1)]
    Q = deque()
    
    for (x, y) in edge:
        G[x].append(y)
        G[y].append(x)

    TRACED[1] = 1
    Q.append(1)

    while Q:
        answer = len(Q)
        for _ in range(len(Q)):
            node = Q.pop()
            for new_node in G[node]:
                if not TRACED[new_node]:
                    Q.appendleft(new_node)
                    TRACED[new_node] = 1
        if not Q: return answer
