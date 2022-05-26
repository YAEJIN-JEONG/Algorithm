# https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations.sort(reverse=True)

    answer = 0
    for i, citation in enumerate(citations):
        answer = max(answer, min(i + 1, citation))

    return answer
