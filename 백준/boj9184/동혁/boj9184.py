li=[[[0] * 21 for _ in range(21)] for __ in range(21)]

def abc(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return abc(20,20,20)
    if li[a][b][c]:
        return li[a][b][c]
    if a<b<c:
        li[a][b][c] = abc(a,b,c-1) + abc(a,b-1,c-1) - abc(a,b-1,c)
        return li[a][b][c]
    li[a][b][c] = abc(a-1,b,c) + abc(a-1,b-1,c) + abc(a-1,b,c-1) - abc(a-1,b-1,c-1)
    return li[a][b][c]

while True:
    a,b,c=map(int,input().split(" "))
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {abc(a,b,c)}')