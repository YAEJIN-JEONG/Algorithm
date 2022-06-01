#https://www.acmicpc.net/problem/1531
n,m = map(int, input().split())
picture = [[0]*100 for x in range(100)]

answer = 0
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(x1,x2+1):
        for k in range(y1,y2+1):
            picture[j-1][k-1]+=1

for i in range(100):
    for j in range(100):
        if picture[i][j] > m:
            answer +=1

print(answer)
