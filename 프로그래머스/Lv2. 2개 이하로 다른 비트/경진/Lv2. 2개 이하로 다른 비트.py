# https://programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    answer = []
    for n in numbers:
        bit = list(bin(n)[2:])

        # 이진수로 바꿨을 때 '0' 이 존재하는 경우
        if '0' in bit:
            for i in range(len(bit) - 1, -1, -1):
                # 가장 작은 '0'인 자리수를 1로 바꿈
                if bit[i] == '0':
                    bit[i] = '1'
                    # 범위를 벗어나지 않으면 그 아래 자리수를 0으로 바꿈
                    if i + 1 < len(bit):
                        bit[i + 1] = '0'
                    break
            answer.append(int(''.join(bit), 2))
        else:
            # 이진수로 바꿨을 때 0이 존재하지 않는 경우
            num = '10' + '1' * (len(bit) - 1)
            answer.append(int(num, 2))

    return answer
