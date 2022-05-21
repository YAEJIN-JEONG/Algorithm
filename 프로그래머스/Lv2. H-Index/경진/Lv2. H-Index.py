# https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations.sort(reverse=True)

    answer = 0
    for i, citation in enumerate(citations):
        if i + 1 >= citation:
            answer = max(answer, citation)
        else:
            answer = max(answer, i + 1)

    return answer
