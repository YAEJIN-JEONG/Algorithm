from itertools import combinations

def solution(relation):
    N, M = len(relation), len(relation[0])
    candidates, uniques = [], []
    
    # 후보키 후보
    for amount in range(1, M + 1):
        candidates.extend([set(c) for c in combinations(range(M), amount)])

    for key in candidates:
        db = set()
        for data in relation:
            db.add(tuple(data[idx] for idx in key))
        if len(db) != N or not is_unique(key, uniques): continue
        uniques.append(key)
    return len(uniques)

def is_unique(candidate, unique_keys):
    for key in unique_keys: 
        if key.issubset(candidate): return False
    return True
