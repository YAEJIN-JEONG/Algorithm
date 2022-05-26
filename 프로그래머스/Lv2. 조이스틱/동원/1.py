answer = 1000000000
N, traced = 0, set()

def solution(name):
    global N
    updown, N = 0, len(name)
    positions = [0] + [i+1 for i, v in enumerate(name[1:]) if v != 'A']

    # up_down
    for p in positions:
        updown += min(ord(name[p])-ord('A'), ord('Z')-ord(name[p])+1)
    if not updown: return 0

    # dfs
    traced.add(0)
    dfs(positions, 0, updown)
    return answer

def dfs(positions, cur_pos, cur):
    global answer

    if len(traced) == len(positions):
        answer = min(answer, cur)
        return

    for n in positions:
        if n in traced: continue
        
        n_cur = cur
        if cur_pos > n: n_cur += min(cur_pos-n, N-cur_pos+n)
        else: n_cur += min(n-cur_pos, cur_pos+N-n)
        if n_cur >= answer: continue
            
        traced.add(n)
        dfs(positions, n, n_cur)
        traced.remove(n)