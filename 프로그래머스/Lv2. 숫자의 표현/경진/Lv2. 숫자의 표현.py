# https://programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    seq = [i for i in range(n + 1)]

    # right pointer, 누적 합, 정답
    rp, total, answer = 0, 0, 0

    # left pointer
    for lp in range(len(seq)):
        total -= seq[lp]

        while total < n and rp < len(seq):
            total += seq[rp]
            rp += 1

        if total == n:
            answer += 1

    return answer
