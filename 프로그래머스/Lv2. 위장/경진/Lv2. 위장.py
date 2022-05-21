# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    hash_table = {}

    # 카테고리별 카운트
    for _, category in clothes:
        hash_table[category] = hash_table.get(category, 0) + 1

    answer = 1
    # 하나의 카테고리에서 고를 수 있는 개수 모두 곱하기
    for k, v in hash_table.items():
        answer *= v + 1

    # 아무것도 안 입는 경우 빼기
    return answer - 1
