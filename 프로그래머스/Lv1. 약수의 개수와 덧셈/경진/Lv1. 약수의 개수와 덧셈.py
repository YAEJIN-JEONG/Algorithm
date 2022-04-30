# https://programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    answer = 0
    # left ~ right
    for i in range(left, right + 1):
        # 약수 개수
        cnt = 0

        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        # 홀수인지 짝수인지에 따라 분기
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer
