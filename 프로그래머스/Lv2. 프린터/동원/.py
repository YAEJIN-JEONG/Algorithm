from collections import deque

def solution(priorities, location):
    cur_max = sorted(priorities)
    documents = deque(range(len(priorities)))
    seq = 1
    
    while documents:
        document = documents.popleft()
        
        if priorities[document] != cur_max[-1]:
            documents.append(document)
            continue
        if document == location: return seq
        cur_max.pop()
        seq += 1
    return len(priorities)
