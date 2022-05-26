# https://programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    # 스택
    answer = []

    for n in number:
        # (head >= n)가 될 때 까지 pop (단, k 가 0보다 커야함)
        while answer and k > 0 and int(answer[-1]) < int(n):
            answer.pop()
            k -= 1
        answer.append(n)

    # k가 남아있으면 마지막에 빼주기
    return ''.join(answer if k == 0 else answer[:-k])
