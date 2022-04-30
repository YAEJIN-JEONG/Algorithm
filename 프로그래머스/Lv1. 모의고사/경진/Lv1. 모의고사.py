# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    # 찍기 패턴 3가지
    pattern = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    # 점수
    score = [0, 0, 0]
    answer = []

    for i in range(len(answers)):
        # i 번째 항목은 각자 패턴의 길이로 나눈 나머지 index 에 있는 값으로 찍음
        for j in range(len(pattern)):
            if pattern[j][i % len(pattern[j])] == answers[i]:
                score[j] += 1

    # 정답 리스트 만들기
    max_score = max(score)
    for i in range(len(score)):
        if score[i] == max_score:
            answer.append(i + 1)

    return answer
