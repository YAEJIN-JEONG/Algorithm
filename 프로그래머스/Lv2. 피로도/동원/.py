from itertools import permutations

def solution(k, dungeons):
    cases = permutations(dungeons, len(dungeons))
    answer = 0

    for case in cases:
        stemina = k
        res = 0
        for required, consume in case:

            if stemina >= required:
                stemina -= consume
                res += 1
            else:
                break
        answer = max(answer, res)
    return answer
