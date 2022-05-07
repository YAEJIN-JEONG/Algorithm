# https://programmers.co.kr/learn/courses/30/lessons/17682
# [1차] 다트 게임
def solution(dart_result):
    score, effect = [], []
    # 얼마 제곱할 지
    sdt = {'S': 1, 'D': 2, 'T': 3}

    num = ''
    for c in dart_result:
        # 현재 score 의 마지막 인덱스
        last_index = len(score) - 1

        if c == '*':
            score[last_index] *= 2
            # 첫번째 세트가 아니면 이전 세트 점수도 2배
            if last_index > 0:
                score[last_index - 1] *= 2
        elif c == '#':
            score[last_index] *= -1
            # '*' 효과를 받은 적이 있으면 이전 세트 점수도 -1배
            if '*' in effect:
                score[last_index - 1] *= -1
        elif c.isnumeric():
            # 숫자면 num 에 저장
            num += c
        else:
            # 'S', 'D', 'T' 중 하나 나오면 점수 추가
            score.append(int(num) ** sdt[c])
            num = ''

    return sum(score)
