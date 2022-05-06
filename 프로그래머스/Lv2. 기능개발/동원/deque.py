from collections import deque

def solution(progresses, speeds):
    result = []
    queue = deque(zip(progresses, speeds))

    while queue:
        res = 0
        for i in range(len(queue)):
            p, s = queue.popleft()
            p += s
            if p >= 100 and res == i: res += 1
            else: queue.append((p, s))
        if res: result.append(res)
    return result
