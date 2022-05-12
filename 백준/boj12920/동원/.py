import sys

# init
input = sys.stdin.readline
N, MAX_W = map(int, input().split())
Stuffs = []
for _ in range(N):
    v, c, k = map(int, input().split())
    p = 1
    while k:
        m = min(k, p)
        Stuffs.append((v*m, c*m))
        k -= m
        p *= 2
N = len(Stuffs)

def solution():
    db = [0] * (MAX_W+1)
    for v, c in Stuffs:
        for w in range(MAX_W, v-1, -1):
            db[w] = max(db[w-v]+c, db[w])
    print(db[MAX_W])

solution()
