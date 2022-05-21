from collections import defaultdict
from itertools import product
from bisect import bisect_left

def solution(info, query):
    db = defaultdict(list)
    info = sorted([i.split() for i in info], key=lambda x : int(x[-1]))
    answer = []
    
    for i in info:
        columns = [("-", column) for column in i[:-1]]
        for key in product(*columns):
            db[key].append(int(i[-1]))

    for q in query:
        q = q.split()
        q, score = (q[0], q[2], q[4], q[6]), int(q[7])
        q_result = db[q]
        answer.append(len(q_result) - bisect_left(q_result, score))
    return answer
