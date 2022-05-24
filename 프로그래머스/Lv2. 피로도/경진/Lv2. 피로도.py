# https://programmers.co.kr/learn/courses/30/lessons/87946
import itertools


# k: 피로도, dungeons: ["최소 필요 피로도", "소모 피로도"]
def solution(k, dungeons):
    answer = 0
    # 던전을 도는 모든 순서 (순열)
    for p in itertools.permutations(range(len(dungeons))):
        k_now, cnt = k, 0

        for i in p:
            min_k, spend_k = dungeons[i]

            if k_now >= min_k:
                k_now -= spend_k
                cnt += 1
            else:
                break
        # 최소값 갱신
        answer = max(answer, cnt)

    return answer
