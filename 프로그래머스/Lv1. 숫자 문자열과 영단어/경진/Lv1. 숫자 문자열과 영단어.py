# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    # 인덱스를 숫자로 이용
    num_to_eng = ['zero', 'one', 'two', 'three', 'four',
                  'five', 'six', 'seven', 'eight', 'nine']

    # 'zero' ~ 'nine' 까지 포함된 문자열을 숫자로 치환
    for i in range(len(num_to_eng)):
        s = s.replace(num_to_eng[i], str(i))

    return int(s)
