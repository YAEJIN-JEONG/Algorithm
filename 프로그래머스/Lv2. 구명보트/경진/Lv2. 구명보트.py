# https://programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    people.sort()
    answer = 0

    # 투 포인터
    left, right = 0, len(people) - 1
    while left <= right:
        # 2명까지 태울 수 있음.
        # 구조하지 않은 사람중 가장 가벼운 사람과 가장 무거운 사람 합 확인
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1

    return answer
