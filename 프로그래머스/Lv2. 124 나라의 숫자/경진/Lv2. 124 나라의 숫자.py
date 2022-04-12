# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    # 사용 숫자 리스트, 3진법 변경을 위한 나머지, 정답
    nums, remains, answer = [1, 2, 4], [], ''

    # n의 3진법 표현 위한 나머지 구하기
    # 0은 표현하지 않음 -> 기본 3진법 보다 같은 자릿수에서 하나 더 표현 가능 -> n 대신 n - 1 로 생각
    while n > 0:
        remains.append((n - 1) % 3)
        n = (n - 1) // 3
    # 3진법 표현은 나머지 배열의 역순, (나머지 -> 사용 숫자)로 변경
    for i in remains:
        answer = str(nums[i]) + answer

    return answer
