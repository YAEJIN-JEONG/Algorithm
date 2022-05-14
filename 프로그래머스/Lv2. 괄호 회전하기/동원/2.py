from collections import deque

def solution(s):
    left = {"[", "(", "{"}
    check = {"]": "[", ")": "(", "}": "{"}
    s = deque(s)
    N = len(s)
    stack = []

    for _ in range(N):
        correct = True
        res = 0
        
        for c in s:
            if c in left: stack.append(c)
            elif not stack or stack[-1] != check[c]: 
                correct = False
                break
            else: 
                stack.pop()
                res += (len(stack) == 0)

        if correct and not stack: return res
    
        stack.clear()
        s.append(s.popleft())
    return 0
