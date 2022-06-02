# https://programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        # 선행 스킬 트리 큐로 만들기
        q = list(skill)

        # 선행 조건이 있는 스킬인 경우 front 와 비교
        for s in skill_tree:
            if s in skill and s != q.pop(0):
                break
        else:
            answer += 1

    return answer
