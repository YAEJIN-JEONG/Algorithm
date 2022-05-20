# https://programmers.co.kr/learn/courses/30/lessons/42890
import itertools


def solution(relation):
    row, col = len(relation), len(relation[0])

    # 후보키
    candidate = []
    # 1 ~ 속성 개수 만큼 뽑는 조합
    for i in range(1, col + 1):
        # i 개 뽑는 조합
        for comb in itertools.combinations(range(col), i):
            # 현재 조합의 부분집합이 후보키에 포함되어 있으면 안됨 (최소성 검사)
            for c in candidate:
                if c < set(comb):
                    break
            else:
                # 유일성 검사
                tuple_now = set()
                for j in range(row):
                    tuple_now.add(''.join([relation[j][attr] for attr in comb]))
                # 유일성 만족하면 후보키에 추가
                if row == len(tuple_now):
                    candidate.append(set(comb))

    return len(candidate)
