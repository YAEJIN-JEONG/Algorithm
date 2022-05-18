#dfs로 진행
def dfs(numbers,target,depth):
    #타겟과 일치하는 경우
    answer = 0

    #단말 노드까지 탐색한 경우
    if depth == len(numbers):
        #타겟과 덧셈의 결과가 같은 경우 1 반환 아니면 0 반환
        if sum(numbers) == target:
            return 1
        else:
            return 0

    #단말노드까지 탐색하지 못한경우
    else:
        #덧셈일 경우 다음 노드로 탐색 진행
        answer += dfs(numbers,target,depth+1)

        #현제 노드를 음수로 바꾸고 탐색 진행
        numbers[depth] *= -1
        answer += dfs(numbers,target,depth+1)
    return answer

def solution(numbers, target):
    answer = 0
    return dfs(numbers,target,0)