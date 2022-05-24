# https://programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    # 이전 단어, 사용한 단어
    prev, used = words[0], {words[0]}

    for i in range(1, len(words)):
        # 사용한 단어가 아니고, 규칙에 맞는 경우
        if words[i] in used or prev[-1] != words[i][0]:
            return [i % n + 1, i // n + 1]

        used.add(words[i])
        prev = words[i]

    return [0, 0]
