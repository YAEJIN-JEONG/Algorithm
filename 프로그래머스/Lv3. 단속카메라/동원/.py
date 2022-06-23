from collections import defaultdict

def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    answer = 0
    
    for start, end in routes:
        if camera < start:
            answer += 1
            camera = end
    return answer
