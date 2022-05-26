def solution(s):
    #모든 문자열이 제거되면 1
    answer = 1
    stack = []
    for i in s:
        #아무것도 없으면 비교가 안됨
        if len(stack) == 0:
            stack.append(i)
            continue
        #마지막에 넣었던 원소랑 현제 원소랑 같으면 제거
        if stack[-1] == i:
            stack.pop()
            continue
        else:
            stack.append(i)

    #스택에 뭔가 남아있으면 0
    if len(stack) != 0:
        answer = 0

    return answer