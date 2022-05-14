from collections import deque

def solution(s):
    left = {"[", "(", "{"}
    check = {"]": "[", ")": "(", "}": "{"}
    s = deque(s)
    N = len(s)
    stack = []
    res = 0

    for _ in range(N):
        correct = True
        for c in s:
            if c in left: stack.append(c)
            elif not stack or stack[-1] != check[c]: 
                correct = False
                break
            else: stack.pop()
        if correct and not stack: res += 1
        stack.clear()
        s.append(s.popleft())
    return res
