N = 5
TRACED = [[False]*N for _ in range(N)]
BORDER = {-1, N}

def solution(places):
    return [checked(place) for place in places]

def checked(place):
    place = [list(row) for row in place]
    for i in range(N):
        for j in range(N):
            if place[i][j] == 'P':
                TRACED[i][j] = True
                if not dfs(place, i, j, 0):
                    TRACED[i][j] = False
                    return 0
                TRACED[i][j] = False
    return 1

def dfs(place, i, j, depth):
    if depth == 2: return True
    for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        if ni in BORDER or nj in BORDER or TRACED[ni][nj]:
            continue
        if place[ni][nj] == 'P' and place[i][j] != 'X': return False
        # dfs
        TRACED[ni][nj] = True
        if not dfs(place, ni, nj, depth+1):
            TRACED[ni][nj] = False
            return False
        TRACED[ni][nj] = False
    return True
