from collections import deque
stack = deque()

while True:
    arr = str(input())
    if arr == '.':
        break

    for i in range(len(arr)):

        if arr[i] == '(':
            stack.append('(')
        elif arr[i] == ')':
            if len(stack) == 0:
                print('no')
                break
            elif stack.pop() != '(':
                print('no')
                break

        if arr[i] == '[':
            stack.append('[')
        elif arr[i] == ']':
            if len(stack) == 0:
                print('no')
                break
            elif stack.pop() != '[':
                print('no')
                break

    if i ==(len(arr)-1):
        if len(stack) == 0:
            print('yes')
        else:
            print('no')

    stack.clear()