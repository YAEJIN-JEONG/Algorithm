import re

def solution(s):
    def compress(s, length):
        REGEX = re.compile(f'([a-z]{{{length}}})\\1*')
        answer = 0
        last_match = None
        
        for match in re.finditer(REGEX, s):
            last_match = match
            start, end = match.span()
            count = (end-start) // length
            answer += [len(str(count)), 0][count == 1] + length
        return answer + len(s) - last_match.span()[1]
    return min(compress(s, length) for length in range(1, len(s)//2 + 2))
