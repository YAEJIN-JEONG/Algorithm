# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    # 왼손, 오른손의 처음 위치 (* = 11, # = 12)
    l_pos, r_pos = 10, 12

    for num in numbers:
        # 숫자 0은 11로 생각
        if num == 0:
            num = 11
        # 1, 4, 7 중 하나인 경우
        if str(num) in '147':
            answer += 'L'
        # 3, 6, 9 중 하나인 경우
        elif str(num) in '369':
            answer += 'R'
        # 그 외의 경우 거리 계산
        else:
            # 각각 행과 열의 위치
            xy_num = [(num - 1) // 3, (num - 1) % 3]
            xy_l = [(l_pos - 1) // 3, (l_pos - 1) % 3]
            xy_r = [(r_pos - 1) // 3, (r_pos - 1) % 3]
            # 눌러야하는 숫자와 왼손, 오른손 위치의 차
            l_diff = abs(xy_num[0] - xy_l[0]) + abs(xy_num[1] - xy_l[1])
            r_diff = abs(xy_num[0] - xy_r[0]) + abs(xy_num[1] - xy_r[1])
            # 거리 차에 따른 분기
            if l_diff == r_diff:
                if hand == 'left':
                    answer += 'L'
                else:
                    answer += 'R'
            elif l_diff < r_diff:
                answer += 'L'
            else:
                answer += 'R'
        # 왼손 또는 오른손 위치 갱신
        if answer[-1] == 'L':
            l_pos = num
        else:
            r_pos = num

    return answer
