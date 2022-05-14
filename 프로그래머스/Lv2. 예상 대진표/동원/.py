def solution(N, A, B):
    for _round in range(1, N):
        A, B = (A+1) // 2, (B+1) // 2
        if A == B: return _round
