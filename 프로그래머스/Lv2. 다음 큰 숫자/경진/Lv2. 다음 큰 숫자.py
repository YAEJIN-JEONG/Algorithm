# https://programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    binary = bin(n)[2:]

    # 모든 비트가 1인 수
    if binary.count('0') == 0:
        return int('10' + binary[1:], 2)
    else:
        # 비트 패턴이 '01' 인 가장 오른쪽 인덱스 찾음
        idx = binary.rfind('01')

        if idx == -1:
            # '01' 인 패턴이 없으면 맨 앞 '1' 을 '10' 으로 바꾸고, 뒤의 '1'들 오른쪽으로 쉬프트
            zero, one = binary[1:].count('0'), binary[1:].count('1')
            return int('10' + '0' * zero + '1' * one, 2)
        else:
            # '01' 인 패턴이 있으면 '10' 으로 바꾸고, 뒤의 '1'들 오른쪽으로 쉬프트
            zero, one = binary[idx + 2:].count('0'), binary[idx + 2:].count('1')
            return int(binary[:idx] + '10' + '0' * zero + '1' * one, 2)
