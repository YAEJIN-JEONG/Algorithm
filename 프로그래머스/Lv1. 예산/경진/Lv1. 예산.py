# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    # 예산 오름차순 정렬
    d.sort()
    # 필요 예산이 적은 부서부터 지원
    answer = 0
    for i in d:
        if budget - i >= 0:
            budget -= i
            answer += 1
        else:
            break

    return answer
