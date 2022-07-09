def solution(s):
    N = len(s)
    DB = [[0]*N for _ in range(N)]
    answer = 1
    
    # 1
    for n in range(N):
        DB[n][n] = 1
        
    # 2
    for n in range(N-1):
        if s[n] == s[n+1]:
            DB[n][n+1] = 1
    
    # 3
    for w in range(3, N+1):
        for i in range(N-w+1):
            j = i+w-1
            
            if s[i] == s[j] and DB[i+1][j-1]:
                DB[i][j] = 1
                answer = max(answer, w)
    return answer
