def solution(msg):
    dictionary, answer = {chr(i + ord('A') - 1): i for i in range(1, 27)}, []

    i = 0
    while i < len(msg):
        # dictionary 에 있는 가장 긴 단어 찾기
        for j in range(len(msg) + 1, i, -1):
            substr = msg[i:j]
            if substr in dictionary:
                answer.append(dictionary[substr])
                dictionary[msg[i:j+1]] = len(dictionary) + 1
                i = j
                break

    return answer
