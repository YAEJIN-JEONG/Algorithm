# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer, stack = 0, []

    for move in moves:
        # 첫 행 부터 move 열에 인형이 있는지
        for i in range(0, len(board)):
            # 인형 있으면 뽑기
            if board[i][move-1] != 0:
                # 빈 stack 이 아니고 head 가 뽑은 인형과 같은지 확인 후 분기
                if stack and stack[-1] == board[i][move-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][move-1])
                board[i][move-1] = 0
                break

    return answer
