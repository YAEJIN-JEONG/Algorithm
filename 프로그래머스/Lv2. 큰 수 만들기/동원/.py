def solution(number, k):
    answer = []
    
    for n in number:
        while k and answer and n > answer[-1]:
            answer.pop()
            k -= 1
        answer.append(n)
    return ''.join(answer[:len(number)-k])
